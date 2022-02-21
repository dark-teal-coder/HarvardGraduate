<!-- This is a README file for a project. -->

# Metadata
- <ins>Project Owner</ins>: github.com/dark-teal-coder
- <ins>First Published Date</ins>: 2022-02-21
- <ins>Last Modified Date</ins>: 2022-02-21

# Title 
Job Bank WebScraper and Data Analyzer

# Description 
The project uses Pythonto scrape wage data from Job Bank, to performsimple data analysisand to generate Excel and PDF reports.The data are drawn from the Canadian national job board, which has a huge number of job postings classified by the Canadian National Occupation Classification(NOC)and other related data.

# Installation 
Make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine. [Git-clone the project repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the local machine. Use the command `pip install package_name` or `conda install package_name` to install the necessary Python libraries. Check the top part of the `.py` script file for the list of libraries required. For example, you may need `requests` and `beautifulsoup4` libraries if you see the following lines in the top part of the script file: 
```
import requests
from bs4 import BeautifulSoup
```
Use `python file_name.py` to run the script in a command-line interface (CLI). Or, download an integrated development environment (IDE), such as [Visual Studio Code](https://code.visualstudio.com/download), to run the script. There will be a "Run" button in the top right corner of the opened script file. 

# Credits 

## Contributors 
1. [DarkTealCoder](https://github.com/dark-teal-coder)

## References 
### Lecture Materials 
1. CSCI E-7 Introduction to Python lecture materials by Jeff Parker from Harvard University 
### Data: 
2. Canada's National Occupation Code (NOC): https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/find-national-occupation-code.html#noc
### Documentations: 
3. Pandas: https://pandas.pydata.org/docs/reference/index.html#api
4. FPDF: https://pyfpdf.readthedocs.io/en/latest/index.html
### Tutorials: 
5. Beautiful Soup: Build a Web Scraper With Python: https://realpython.com/beautiful-soup-web-scraper-python/
6. Python if \__name__ == \__main__ Explained with Code Examples: https://www.freecodecamp.org/news/if-name-main-python-example/
7. Convert Text and Text File to PDF using Python: https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
### Solutions: 
8. Ref.: https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
