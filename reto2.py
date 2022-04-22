from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
import json 

url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'

driver = webdriver.Chrome(executable_path='C:\dchrome\chromedriver.exe')

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

tables = soup.find_all('table')
for table in tables:
    tablestxt = table.get_text()
    print(table.next_sibling)
print(tables)
