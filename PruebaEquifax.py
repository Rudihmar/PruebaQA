from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
serv = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service= serv)
driver.maximize_window()

driver.get("https://demoqa.com/webtables")
print(driver.title)
time.sleep(2)

'''añadir usuario'''
add = driver.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/button[1]')
add.click()
print('Añadir usuario')
time.sleep(2)
'''nombre'''
Name = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/input[1]')
Name.click()
Name.send_keys('Rudihmar')
time.sleep(2)
'''apellido'''
lastName = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/input[1]')
lastName.click()
lastName.send_keys('Suarez')
time.sleep(2)
'''mail'''
mail = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[3]/div[2]/input[1]')
mail.click()
mail.send_keys('rudysuarez@prueba.com')
time.sleep(2)
'''edad'''
age = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[4]/div[2]/input[1]')
age.click()
age.send_keys('19')
time.sleep(2)
'''salario'''
salary = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[5]/div[2]/input[1]')
salary.click()
salary.send_keys('1200')
time.sleep(2)
'''departamento'''
department = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[6]/div[2]/input[1]')
department.click()
department.send_keys('QA funcional')
time.sleep(2)

'''click submit'''
submit = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]')
submit.click()
driver.execute_script("window.scrollTo(0, window.scrollY + 50)")
time.sleep(2)

'''click editar'''
editar = driver.find_element(By.CSS_SELECTOR,'div.body-height:nth-child(2) div.container.playgound-body div.row div.col-12.mt-4.col-md-6:nth-child(2) div.web-tables-wrapper:nth-child(2) div.ReactTable.-striped.-highlight div.rt-table div.rt-tbody div.rt-tr-group:nth-child(4) div.rt-tr.-even div.rt-td:nth-child(7) div.action-buttons span.mr-2:nth-child(1) > svg:nth-child(1)')
editar.click()
print('Editar usuario')
time.sleep(10)

'''editar edad'''
age1 = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[4]/div[2]/input[1]')
age1.click()
age1.clear()
time.sleep(2)
age1.send_keys('25')
time.sleep(2)

'''click submit'''
add = driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]')
add.click()
time.sleep(2)