import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get('https://www.dominospizza.cl')
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='iniciaSesion']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='loginPopup']/div[3]/div[2]/div/div[3]/span/span/u").click()
time.sleep(3)

psw = driver.find_element(By.ID, "email_reset_password")
psw.send_keys("abelito.colocolo@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='submit-reset-password']").click()
time.sleep(5)
driver.close()