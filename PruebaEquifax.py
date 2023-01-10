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