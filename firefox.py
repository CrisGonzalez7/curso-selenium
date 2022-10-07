from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="/usr/local/share/geckodriver")

driver.get("https://jardinesparaiso.cl")

print("Bienvenido a Selenium")

driver.close()