<!-- This is a README file for a project. -->

# Metadata
- <ins>Project Owner</ins>: [@dark-teal-coder](github.com/dark-teal-coder)
- <ins>First Published Date</ins>: 2022-02-21
- <ins>Last Modified Date</ins>: 2022-03-01

# Project 
- <ins>Title</ins>: Job Bank Web Scraper and Data Analyzer
- <ins>Difficulty</ins>:
  - [ ] Beginner
  - [x] Intermediate
  - [ ] Advanced
- <ins>Scale</ins>: 
  - [ ] Small
  - [x] Medium
  - [ ] Big

# Description 
The project uses Python to scrape wage data from [Job Bank](https://www.jobbank.gc.ca/home), to perform simple data analysis and to generate Excel and PDF reports. The data are drawn from the Canadian national job board, which has a huge number of job postings classified by the Canadian National Occupation Classification (NOC) and other related data.

# Installation 

## Tools
- Text Editor or Integrated Development Environment (IDE)
  - You can [download the famous text editor Notepad++](https://notepad-plus-plus.org/downloads/). 
  - Or, you can [download the popular IDE Visual Studio Code (VS Code)](https://code.visualstudio.com/download). 
- Python 3
  - You can [install Python 3 from python.org](https://www.python.org/downloads/). 
- Python Package Installer/Manager `pip`
  - If you installed Python from [python.org](https://www.python.org/), you should already have `pip`. If it is not installed, you can use the command `py -m ensurepip --default-pip` to bootstrap it from the standard library. If you are using Linux, you will have to [install the package manager separately](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/). You can find out more about the `pip` tool [here](https://pip.pypa.io/en/stable/getting-started/). 
- Command-line interface (CLI) 
  - You can [install the open-source PowerShell on Windows, Linux and macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) if you do not have or want to use a pre-installed CLI on your local machine. 

## Description
Check if you have Python installed using the command `python --version`, or simply, `python version`, in the CLI. [Git-clone the project repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the local machine. Use the command `py -m pip install package_name` to install the necessary Python libraries. Check out [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) to learn more about `pip install`. Check the top part of the `.py` script file for the list of libraries required. For example, you may need `requests` and `beautifulsoup4` libraries if you see the following lines in the top part of the script file: 
```
import requests
from bs4 import BeautifulSoup
```
If `pip` fails to locate the relevant packages, you may find it at [Python Package Index (PyPI)](https://pypi.org/). Use `python file_name.py` to run the script in a CLI. Or, use an IDE, such as VS Code, to run the script. There will usually be a [Run] button in the top right corner of the opened script file. 

# Credits 

## Contributors 
1. [@dark-teal-coder](github.com/dark-teal-coder)

## References 
### Lecture Materials:
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
8. StackOverflow: https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
