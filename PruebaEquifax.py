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
