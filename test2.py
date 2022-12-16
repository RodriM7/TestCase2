import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=options)
driver.get("https://lavandanatural.com/")
time.sleep(2)

icono = driver.find_element(By.ID, "auth")
icono.click()
time.sleep(1)

login = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[2]/div[1]/div/a[2]")
login.click()
time.sleep(3)

mail = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[4]/form/div[1]/input")
mail.send_keys("rmunoz_probar@yahoo.com")
time.sleep(2)

passw = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[4]/form/div[2]/input")
passw.send_keys("probar123456")
passw.send_keys(Keys.ENTER) # Inicia sesion
time.sleep(2)

inicio = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[1]/a")
inicio.click()
time.sleep(2)

barra = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[1]/form/input")
barra.click()
barra.send_keys("acondicionador")
time.sleep(5)

requirement = ()    
labelObtained = ()      

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")

#validar que el producto que sea ingresa en la barra de busqueda aparezca cuando el cliente es redireccionado
linkCuartoProducto = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[1]/div/ul/li[4]/a/div[2]/p[1]")   


labelCuartoProducto =  driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[1]/div/ul/li[4]/a/div[2]/p[1]").text

labelObtained = labelCuartoProducto

print(labelObtained)

requirement = 'ACONDICIONADOR'

compareLabels()

cuartoProducto = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[1]/div/ul/li[4]/a/div[2]/p[1]")
cuartoProducto.click() 
time.sleep(3)

agregar = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[2]/div/form/div[4]/div/div/input")
agregar.click()
time.sleep(2)

continuar = driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[4]/div/div[8]/div[2]/a")
continuar.click() # Continuar con la compra
time.sleep(3)

inicio = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[1]/a")
inicio.click() # Vuelve al inicio
time.sleep(3)

driver.close()