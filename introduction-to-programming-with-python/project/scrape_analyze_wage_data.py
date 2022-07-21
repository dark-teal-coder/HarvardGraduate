## GitHub: dark-teal-coder 
import pandas as pd
import numpy as np 
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import datetime
import string
import os 


## Get datetime information 
current_datetime = datetime.datetime.now()
current_year = current_datetime.year
## Get the running script path 
script_path = os.path.dirname(os.path.abspath(__file__))
## Get the current working directiory 
cwd = os.path.abspath(os.getcwd())
# print(script_path, cwd)


def read_noc(noc_filepath): 
    """This function reads a data file containing a table of National Occupational Classification (NOC) codes related to computer 
    science and information technology jobs and returns the data in DataFrame format."""
    try: 
        ## Use Pandas to read in csv file 
        ## Python parsing engine for RegEx delimiters
        df_noc = pd.read_csv(noc_filepath, sep=', ', header=0, engine='python') 
    except FileNotFoundError: 
        print(f"The following file cannot be found:", noc_filepath, sep='\n')
    except: 
        print("An unknown error occurs while reading in the following file causing the program to exit prematurely:", noc_filepath, 
        sep='\n')
    else: 
        ## Unify the headers 
        df_noc.columns = df_noc.columns.str.lower()
        ## Trim leading and ending spaces in the headers 
        ## Ref.: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html
        ## (inplace=True) means not to return a new DataFrame
        df_noc.rename(columns=lambda x: x.strip(), inplace=True) 
        # print(df_noc)
        return df_noc


def get_page(url_code, c): 
    """This function scrapes wage data of 10 tech occupations classified by NOC from Job Bank and returns the data list."""
    url_base = "https://www.jobbank.gc.ca/wagereport/occupation/"
    ## Add URL code to the end of the base URL to go to different wage report pages on Job Bank  
    url = url_base + str(url_code[c])
    html_response = requests.get(url)
    ## The .content attribute holds raw bytes, which can be decoded better than the .text attribute.
    html_doc = BeautifulSoup(html_response.content, 'html.parser')
    # print(html_doc)
    data_list = []
    # wage_table = html_doc.find(id="wage-occ-report")
    # print(wage_table)
    nation_wages = html_doc.find("tr", class_="areaGroup national")
    data_list.append(nation_wages.text.strip().split())
    province_wages = html_doc.find_all("tr", class_="areaGroup province prov")
    for prov_wage in province_wages: 
        data_list.append(prov_wage.text.strip().rsplit(maxsplit=3))
    # print([row for row in data_list])
    return data_list 


def write_excel(filepath_in, df_noc, url_code): 
    writer = pd.ExcelWriter(filepath_in, engine='xlsxwriter')
    headers_nation = ['NOC', 'Occupation', 'URL Code', 'Low', 'Mid', 'High']
    headers_province = ['Province', 'Low', 'Mid', 'High']
    ## Each iteration will scrape a webpage and change the data for 1 NOC into a DataFrame
    df_tech_wages_ca = pd.DataFrame()
    df_tech_wages_prov = pd.DataFrame()
    for i in range(len(url_code)): 
        noc = f"NOC{df_noc.loc[i, 'noc']}"
        data_list = get_page(url_code, i)
        # print(df_noc.loc[i])
        df_wage_table = pd.DataFrame(data_list, columns =['area', 'low', 'mid', 'high'])
        # df_wage_table = pd.to_numeric(df_wage_table, errors='coerce')
        # df_wage_table = df_wage_table.astype({'low': 'float64', 'mid': 'float64', 'high': 'float64'}, errors='ignore')
        print(df_wage_table)
        ## Get the national wage data from the 1st row of each DataFrame 
        df_can_wage = df_wage_table.iloc[[0]]
        df_career = df_noc.iloc[[i]].reset_index(drop=True)
        df_can_wage_career = pd.concat([df_career, df_can_wage], axis=1)
        df_tech_wages_ca = df_tech_wages_ca.append(df_can_wage_career, ignore_index=True)
        ## Drop the 1st row containing national wage data 
        df_wage_table = df_wage_table.drop(0)
        df_wage_table.to_excel(writer, sheet_name=noc, header=headers_province, index=False)
        df_wage_table['high'] = pd.to_numeric(df_wage_table['high'], errors='coerce')
        # df_wage_table = df_wage_table.replace(np.nan, 0, regex=True)
        # df_wage_table['high'] = df_wage_table['high'].astype(int)
        # print (df_wage_table.dtypes)
        occupation_highest = df_wage_table['high'].max(skipna=True)
        province = df_wage_table.loc[df_wage_table['high']==occupation_highest, 'area'].values[0]
        dict = {'NOC':f"{df_noc.loc[i, 'noc']}", 'Occupation':f"{df_noc.loc[i, 'occupation']}", 
            'Highest Hourly Wage': occupation_highest, 'Province': province}
        df_tech_wages_prov = df_tech_wages_prov.append(dict, ignore_index=True) 
        ## Add formatting 
        workbook = writer.book
        worksheet = writer.sheets[noc]
        ## Ref.: https://xlsxwriter.readthedocs.io/format.html
        cell_format = workbook.add_format({'align':'left'})
        cell_format.set_bg_color('#008080')
        eng_alpha_upper = string.ascii_uppercase
        cell_row_num = df_wage_table[df_wage_table['high']==occupation_highest].index.values[0] + 1
        cell_col_num = df_wage_table.columns.get_loc('high')
        cell_col_letter = eng_alpha_upper[cell_col_num]
        excel_cell = cell_col_letter + str(cell_row_num)
        worksheet.write(excel_cell, occupation_highest, cell_format)
    ## Remove 'area' column
    df_tech_wages_ca = df_tech_wages_ca.drop(columns=['area'])
    ## Drop NOC 213 row as managerial level always pays higher than others 
    df_tech_wages_ca = df_tech_wages_ca.drop(0)
    ## Write national tech career wage data to Excel 
    df_tech_wages_ca.to_excel(writer, sheet_name='Canada Tech Career', header=headers_nation, index=False)
    print(df_tech_wages_prov)
    df_tech_wages_prov.to_excel(writer, sheet_name='Highest Wage Province by NOC', header=True, index=False)
    writer.sheets['Highest Wage Province by NOC'].activate()
    writer.save()
    return df_tech_wages_ca


def obtain_pdf_data(df_tech_wages_ca): 
    ## Obtain some national wage data values 
    high_max = df_tech_wages_ca['high'].max(skipna=True)
    high_min = df_tech_wages_ca['high'].min(skipna=True)
    low_max = df_tech_wages_ca['low'].max(skipna=True)
    low_min = df_tech_wages_ca['low'].min(skipna=True)
    high_max_job = df_tech_wages_ca.loc[df_tech_wages_ca['high']==high_max, 'occupation'].values[0]
    high_max_noc = df_tech_wages_ca.loc[df_tech_wages_ca['high']==high_max, 'noc'].values[0]
    high_min_job = df_tech_wages_ca.loc[df_tech_wages_ca['high']==high_min, 'occupation'].values[0]
    high_min_noc = df_tech_wages_ca.loc[df_tech_wages_ca['high']==high_min, 'noc'].values[0]
    low_max_job = df_tech_wages_ca.loc[df_tech_wages_ca['low']==low_max, 'occupation'].values[0]
    low_max_noc = df_tech_wages_ca.loc[df_tech_wages_ca['low']==low_max, 'noc'].values[0]
    low_min_job = df_tech_wages_ca.loc[df_tech_wages_ca['low']==low_min, 'occupation'].values[0]
    low_min_noc = df_tech_wages_ca.loc[df_tech_wages_ca['low']==low_min, 'noc'].values[0]
    ## Text for tech career wage report 
    report_nation = (f"According to the data from the national job board website of Canada Job Bank, the best tech job "
        f"in Canada that pays you the most per hour is {high_max_job}, at CAD{high_max}/hr, while {low_min_job} pays you "
        f"the least, at CAD{low_min}/hr. This result does not include managerial roles in the industry as managerial positions "
        f"in most occupations usually get paid more than their juniors. {high_max_job} job category comes with the national "
        f"occupation classification (NOC) code of NOC{high_max_noc} and {low_min_job} of NOC{low_min_noc}. \n"
        f"\nIf you've just graduated from a computer science or information technology program and are uncertain about "
        f"what type of work you want to do, why don't start with NOC{low_max_noc} {low_max_job}? It's the highest paid "
        f"entry-level tech job, currently paying at CAD{low_max}/hr. You might want to avoid the lowest paid role "
        f"NOC{low_min_noc} {low_min_job} though. But if you're an experienced professional currently working in the field, "
        f"especially if your job falls into NOC{high_min_noc} {high_min_job}, you may consider changing to NOC{high_max_noc}"
        f" {high_max_job}. It's currently the highest paid role for experienced tech workers.")
    return report_nation


def write_pdf(filepath_out, text): 
    """This function is used for generating PDF report(s)."""
    pdf = FPDF()
    pdf.set_margins(5, 5, 5)
    pdf.set_auto_page_break(auto=True)
    pdf.add_page(orientation='P', format='A4')
    pdf.set_font("Courier", style='B', size=12)
    pdf.cell(200, 10, txt=f"Canada Tech Career Wage Report {current_year} Data from Job Bank", ln=1, align='C')
    pdf.ln(10)
    pdf.set_font("Courier", style='I', size=12)
    pdf.cell(200, 10, txt="Reporter: Roxanne Saewong", ln=1, align='R')
    pdf.ln(10)
    pdf.set_font("Courier", size=12)
    pdf.multi_cell(200, 10, txt=text, ln=2, align='L')
    pdf.output(filepath_out, dest='F') 


## Adding this part to prevent some top-level code from being executed when importing modules 
if __name__ == "__main__": 
    df_noc = read_noc(f"{script_path}\input\comp_tech_noc.csv")
    ## Get number of rows of DataFrame 
    df_noc_len = df_noc.shape[0]
    url_code = [df_noc.loc[i, 'url_code'] for i in range(df_noc_len)]
    df_tech_wages_ca = write_excel(f"{script_path}\output\Canada Tech Career Wage Report {current_year}.xlsx", df_noc, url_code)
    report_nation = obtain_pdf_data(df_tech_wages_ca)
    write_pdf(f"{script_path}\output\Canada Tech Career Wage Report {current_year}.pdf", report_nation)
    print("The program has been successfully executed!")
