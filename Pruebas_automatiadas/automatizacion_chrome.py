#imports :)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://feedback.educk.cl/")

#Caso de prueba 1
btncuakcuak = driver.find_element(By.XPATH, "//button['btn-kenay']")  
btncuakcuak.click()
driver.implicitly_wait(1.0)
driver.quit()
  #Por si el primero no funciona
# btncuakcuak.click('btn-kenay')

#Caso de prueba 2
btncuakcuak2 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-3']")
btncuakcuak2.click()
  #Una vez dentro de la sala 3, se debe hacer click en el boton de "Ingresar a la sala" para poder ingresar a "Testing"
btncuakcuak3 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-4']")  
btncuakcuak3.click()
driver.implicitly_wait(1.0)
driver.quit()


#Caso de prueba 3
btncuakcuak4 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-3']")
btncuakcuak4.click('btn-go-to-sala-3')

  #Una vez dentro de la sala 3, se debe hacer click en el boton de "Ingresar a la sala" para poder ingresar a "Testing"
btncuakcuak5 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-4']")
btncuakcuak5.click()
#Rellenar el formulario
with open('datos.txt') as file:
    for i, line  in enumerate(file):
        name = (line)
        separador = ","   
        dividir = name.split(separador)
        try:
            getdata = dividir[1]
            user = dividir[0]
            app_pat = dividir[1]
            feedback = dividir[0]
        except IndexError:
            getdata = 'null'
driver.implicitly_wait(1.0)

if getdata == True:
    contador = 0
    driver.find_element(By.ID, "login").send_keys(user)
    time.sleep(2.0)
    driver.find_element(By.ID, "apppat").send_keys(app_pat)
    time.sleep(2.0)
    driver.find_element(By.ID, "feed").send_keys(feedback)
    time.sleep(2.0)
    contador = contador + 2
    print("El ciclo ha terminado, contador vale: ", contador) 
    file.close()
else:
    print("No hay mas datos")
    file.close()
print(user)
print(app_pat)
print(feedback)
driver.quit() 



#Caso de prueba 4
btncuakcuak6 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-3']")
btncuakcuak6.click()

  #Una vez dentro de la sala 3, se debe hacer click en el boton de "Ingresar a la sala" para poder ingresar a "Testing"
btncuakcuak7 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-4']")
btncuakcuak7.click('btn-go-to-sala-4')
driver.implicitly_wait(1.0)
  #Una vez dentro de la sala 3, se debe hacer click en el boton de "Ingresar a la sala" para poder ingresar a "Testing"
btncuakcuak8 = driver.find_element(By.XPATH, "//button['btn-go-to-sala-4']")
btncuakcuak8.click('btn-go-to-sala-4')
#Rellenar el formulario
with open('datos.txt') as file:
    for i, line  in enumerate(file):
        name = (line)
        separador = ","   
        dividir = name.split(separador)
        try:
            getdata = dividir[1]
            user = dividir[0]
            app_pat = dividir[1]
            feedback = dividir[0]
        except IndexError:
            getdata = 'null'
driver.implicitly_wait(1.0)

if getdata == True:
    contador = 0
    driver.find_element(By.ID, "login").send_keys(user)
    time.sleep(2.0)
    driver.find_element(By.ID, "apppat").send_keys(app_pat)
    time.sleep(2.0)
    driver.find_element(By.ID, "feed").send_keys(feedback)
    time.sleep(2.0)
    contador = contador + 5
    print("El ciclo ha terminado, contador vale: ", contador) 
    file.close()
else:
    print("No hay mas datos")
    file.close()
print(user)
print(app_pat)
print(feedback)
driver.quit()


#Caso de prueba 5 
  #Aqui llamamos el titulo de la pagina
print(driver.title)
  #aqui llamamos a la url del footer
url = driver.get('http://www.bemtorres.win')
#Salida de la prueba
driver.quit()