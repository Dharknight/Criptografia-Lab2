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
    #users_mails=["abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    #"abelito.colocolo@gmail.com","baullozaabel@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl"]
    #password=["12345678Ab","123456ABeL","1ABElsoyyo","2ABElsoyyo","SoyelAbel22","Vestiai2022cripto","mequededormidoA1"]

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://es.vestiairecollective.com/')
    time.sleep(5)  
    driver.find_element(By.ID, "popin_tc_privacy_button_2").click()
    time.sleep(2) 
    driver.find_element(By.XPATH, "//*[@id='user-login']/vc-auth-button/button").click()
    time.sleep(2) 
    email = driver.find_element(By.ID, "user_email")
    email.clear()
    email.send_keys("juanpedro@outlook.cl")
    passw = driver.find_element(By.ID,"user_password")
    passw.clear()
    passw.send_keys("mequededormidoA1")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
    time.sleep(3)

    email = driver.find_element(By.ID, "user_email")
    email.clear()
    email.send_keys("abelito.colocolo@gmail.com")
    passw = driver.find_element(By.ID,"user_password")
    passw.clear()
    passw.send_keys("12345678Ab")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
    time.sleep(3)

    email = driver.find_element(By.ID, "user_email")
    email.clear()
    email.send_keys("emilo@gmail.com")
    passw = driver.find_element(By.ID,"user_password")
    passw.clear()
    passw.send_keys("kxxahypi.")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
    time.sleep(3)

    email = driver.find_element(By.ID, "user_email")
    email.clear()
    email.send_keys("raulautotrans@gmail.com")
    passw = driver.find_element(By.ID,"user_password")
    passw.clear()
    passw.send_keys("TK0VSHW9WLVG")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
    time.sleep(3)

    email = driver.find_element(By.ID, "user_email")
    email.clear()
    email.send_keys("baullozaabel@gmail.com")
    passw = driver.find_element(By.ID,"user_password")
    passw.clear()
    passw.send_keys("Vestiaicripto2022.")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
    time.sleep(5)
    driver.close()






    #for i in password:
    #    for j in users_mails: 
            
    #        email = driver.find_element(By.ID, "user_email")
    #        email.clear()
    #        email.send_keys(j)
    #        time.sleep(1)
    #        passw = driver.find_element(By.ID,"user_password")
    #        passw.clear()
    #        passw.send_keys(i)
    #        time.sleep(1)
    #        driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
    #        time.sleep(2)

    


    #driver.get('https://es.vestiairecollective.com/reset-password.shtml?t=Z7XDMAZfeqhOXS.vUFeziCGjlPNasvCa')
    
#     email = driver.find_element(By.ID, "identifierId")
#     email.send_keys("baullozaabel@gmail.com")
#     time.sleep(3)

#     driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
#     time.sleep(30)

#     passw = driver.find_element(By.NAME, "password")
#     passw.send_keys("Pegitas2022")
#     driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
#     time.sleep(5)

#     driver.find_element(By.ID, ":2v")
#     time.sleep(2)

#     driver.find_element(By.XPATH, "//*[@id=':nv']/div[1]/table/tbody/tr[4]/th/div/div/a").click()
#     time.sleep(5)

    # driver.find_element(By.ID, "popin_tc_privacy_button_2").click()
    # time.sleep(2)

    # passwn = driver.find_element(By.ID, "user_password")
    # passwn.send_keys("Vestiai2022cripto.")
    # time.sleep(1)
    # passwnc = driver.find_element(By.ID, "user_password_new")
    # passwnc.send_keys("Vestiai2022cripto.")
    # time.sleep(2)

    # driver.find_element(By.XPATH, "//*[@id='form-reset']/button").click()
    # time.sleep(5)


    #email = driver.find_element(By.XPATH, "//*[@id='login-register-auto-flow-input']")
            #email.clear()
            #time.sleep(2)
            #driver.find_element(By.XPATH, "//*[@id='modal-root']/div/div/div/div[2]/div/form/button").click()
            #time.sleep(2)
            #email.send_keys(j)
            #time.sleep(2)
            #pwd = driver.find_element(By.XPATH, "//*[@id='registration-password-field']")
            #pwd = driver.find_element_by_id("registration-password-field")
            #pwd.clear()
            #time.sleep(2)
            #edad = driver.find_element(By.NAME, "ageConfirmation").click()
            #time.sleep(2)
            #term = driver.find_element(By.NAME, "terms").click()
            #pwd.send_keys(i)
            #time.sleep(2)
            #driver.find_element(By.XPATH, "//*[@id='modal-root']/div/div/div/div[2]/div/button").click()
            #time.sleep(2)