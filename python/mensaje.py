from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

name = input("Dame el nombre o el grupo:")
msj = input("que le quieres mandar:")
count = int(input("cuantas veces:"))

input("avisame cuando escanees el código QR")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msj)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
