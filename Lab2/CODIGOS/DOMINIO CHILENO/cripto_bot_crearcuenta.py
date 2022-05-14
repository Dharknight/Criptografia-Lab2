from distutils.spawn import find_executable
from gettext import find
import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get('https://www.dominospizza.cl/')
time.sleep(3)

driver.find_element(By.ID,"iniciaSesion").click()
time.sleep(3)  

driver.find_element(By.XPATH, "//*[@id='loginPopup']/div[3]/div[1]/a[1]").click()
time.sleep(1)
#nombre
nombre = driver.find_element(By.NAME, "user[name]")
nombre.send_keys("Foje")
time.sleep(1)
#apellido
ape = driver.find_element(By.NAME,"user[surname]")
ape.send_keys("Esa")
time.sleep(1)
#email
cor = driver.find_element(By.ID, "email")
cor.send_keys("fojesa1131@eoscast.com") 
time.sleep(1)
#telefono
tel = driver.find_element(By.NAME, "user[phone]")
tel.send_keys("66666666")
time.sleep(1)
#contraseña
contr = driver.find_element(By.ID, "pass")
contr.send_keys("dominospizza")
time.sleep(1)
#confirmarcontraseña
cof = driver.find_element(By.ID, "passConfirmation")
cof.send_keys("dominospizza")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[10]/div/form/div[2]/span/input").click()
time.sleep(10)

driver.close()


