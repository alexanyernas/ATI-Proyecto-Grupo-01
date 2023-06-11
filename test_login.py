from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Creamos una nueva sesion en Chrome
driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.maximize_window()


driver.get("http://127.0.0.1:5000/auth/login")

driver.find_element(By.ID, "alias").send_keys("alexanyernas")
driver.find_element(By.ID, "password").send_keys("Programacion30!98" + Keys.ENTER)

driver.implicitly_wait(100)


driver.quit()