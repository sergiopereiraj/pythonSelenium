import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'

r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.title)

tables = soup.find_all('')
for table in tables:
    tablestxt = table.get_text()
    print(table.next_sibling)
print(tables)