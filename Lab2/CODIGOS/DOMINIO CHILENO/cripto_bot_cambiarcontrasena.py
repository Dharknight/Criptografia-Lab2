import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get('https://www.dominospizza.cl/')
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='iniciaSesion']").click()
time.sleep(2)
usr = driver.find_element(By.ID, "user_email")
usr.send_keys("abelito.colocolo@gmail.com")
time.sleep(2)
psw = driver.find_element(By.ID, "user_password")
psw.send_keys("dominospizza")
time.sleep(2)
driver.find_element(By.ID, "submit-login").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[6]/nav/ul/span/li[1]/a[1]/u").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div/div[1]/a").click()
time.sleep(1)
newpas = driver.find_element(By.ID, "new_password")
newpas.send_keys("dominospizza") 
time.sleep(1)
confpas = driver.find_element(By.ID, "confirm_new_password")
confpas.send_keys("dominospizza") 
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='edit_user_506320']/div/div[3]/div/div[2]/input").click()
time.sleep(5)

driver.close()

#pswn = driver.find_element(By.ID, "password_reset_confirmation")
#pswn.send_keys("dominospizza")
#time.sleep(2)











#driver.find_element(By.XPATH, "//*[@id='edit_user_506340']/div/div[3]/div/div[2]/input").click()
#time.sleep(15)

