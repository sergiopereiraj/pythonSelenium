from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'

driver = webdriver.Chrome(executable_path='C:\dchrome\chromedriver.exe')

driver.get(url)

driver.maximize_window()

# columnas = driver.find_element_by_xpath('//thead/tr/th')

# ides = driver.find_elements_by_xpath('//tbody/tr/td[1]')
ides = driver.find_elements(By.XPATH,'//tbody/tr/td[1]')
razonSociales = driver.find_elements(By.XPATH,'//tbody/tr/td[2]')
paises = driver.find_elements(By.XPATH,'//tbody/tr/td[3]')
datos = driver.find_elements(By.XPATH,'//tbody/tr/td[4]')
vigencias = driver.find_elements(By.XPATH,'//tbody/tr/td[5]')
actualizaciones = driver.find_elements(By.XPATH,'//tbody/tr/td[6]')
estados = driver.find_elements(By.XPATH,'//tbody/tr/td[7]')

lista = []
for i in range(len(ides)):
    temporaly_data = {"No": ides[i].text, "RAZÓN SOCIAL": razonSociales[i].text, "PAÍS": paises[i].text, "DATOS INSCRIPCIÓN": datos[i].text, "VIGENCIA HASTA": vigencias[i].text, "DATOS ÚLTIMA ACTUALIZACIÓN":actualizaciones[i].text, "ESTADO": estados[i].text}
    lista.append(temporaly_data)



data_json = json.dumps(lista, ensure_ascii=False)

print(data_json)


#     temporaly_data = {ides[i].text : ['RAZÓN SOCIAL': razonSociales[i].text, 'PAÍS': paises[i].text, 'DATOS INSCRIPCIÓN': datos[i].text, 'VIGENCIA HASTA': vigencias[i].text, 'DATOS ÚLTIMA ACTUALIZACIÓN':actualizaciones[i].text, 'ESTADO': estados[i].text]}

# for estado in estados:
#     print(estado.text)

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# tables = soup.find_all('table')
