from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
time.sleep(5)

# Mengisi formulir registrasi
driver.find_element(By.ID, "gender-male").click()
driver.find_element(By.ID, "FirstName").send_keys('Ryaas')
driver.find_element(By.ID, "LastName").send_keys('Ishlah')
driver.find_element(By.NAME, "DateOfBirthDay").send_keys("13")
driver.find_element(By.NAME, "DateOfBirthMonth").send_keys("November")
driver.find_element(By.NAME, "DateOfBirthYear").send_keys("2002")
driver.find_element(By.ID, "Email").send_keys('ryaasishlah@gmail.com')
driver.find_element(By.ID, "Password").send_keys('iyas123')
driver.find_element(By.ID, "ConfirmPassword").send_keys('iyas123')

# Mengklik tombol register
driver.find_element(By.ID, "register-button").click()
