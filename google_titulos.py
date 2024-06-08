from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pyautogui


link = 'https://www.google.com'
assunto = 'Inteligência Artificial'

navegador = webdriver.Chrome()
navegador.get(link)
sleep(2)

navegador.find_element('xpath', '//*[@id="APjFqb"]').click()
pyautogui.write(assunto)
pyautogui.press('enter')
titulo = navegador.find_elements(By.TAG_NAME, 'h3')

for title in titulo:
    print(title.text)




