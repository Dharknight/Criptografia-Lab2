import string, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_path = '/usr/local/bin/chromedriver'

if __name__ == "__main__":
    #Variables
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(driver_path, chrome_options=options)
    #users_mails=["abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    #"abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl"]
    #password=["12345678Ab","123456ABeL","1ABElsoyyo","2ABElsoyyo","SoyelAbel22","ELESTRATEGADELFortnite4","mequededormidoA1"]

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://www.dominospizza.cl/')
    time.sleep(3)

    driver.find_element(By.ID,"iniciaSesion").click()
    time.sleep(3)

    mail = driver.find_element(By.ID, "user_email")
    mail.send_keys("abelito.colocolo@gmail.com")
    time.sleep(1)
    passw = driver.find_element(By.ID, "user_password")
    passw.send_keys("dominospizza")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='submit-login']").click()
    time.sleep(5)
    
    driver.close()



