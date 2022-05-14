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
    users_mails=["abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans1@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com","abelito.colocolo@gmail.com","emilo@gmail.com","12345@gmail.com","juanpedro@outlook.cl",
    "lperez@dharmausaha.cl","raulautotrans@gmail.com","info@elrelincho.cl","sherrera@vgi.cl","info@centraltimbres.cl","baullozaabel@gmail.com"]
    password=["12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022.","12345678Ab","mx44zz3","mx226","TK0VSHW9WLVG","kxxahypi","Vestiai2022cripto","cnnzadlb","asasasasa","1212Aeas","Vestiaicripto2022."]

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
    time.sleep(3) 
    
    j=0

    for i in range(0,100):
        #for j in range(0,2):
        email = driver.find_element(By.ID, "user_email")
        email.clear()
        email.send_keys(users_mails[i])
        time.sleep(1)
        passw = driver.find_element(By.ID,"user_password")
        passw.clear()
        passw.send_keys(password[j])
        j=j+1
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='loginForm']/div/button").click()
        time.sleep(1)
    driver.close()