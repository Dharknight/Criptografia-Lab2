import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get('https://es.vestiairecollective.com/')
time.sleep(3)

driver.find_element(By.ID, "popin_tc_privacy_button_2").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='user-login']/vc-auth-button/button").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
time.sleep(3)

psw = driver.find_element(By.ID, "user_login_email")
psw.send_keys("baullozaabel@gmail.com")

driver.find_element(By.XPATH, "//*[@id='test_id']/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/form/button").click()
time.sleep(10)

driver.close()