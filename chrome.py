from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="/usr/local/share/chromedriver")

driver.get("https://jardinesparaiso.cl")

print("Bienvenido a Selenium")
print(driver.title)

driver.close()