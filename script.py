from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
import time
import pyautogui
from os import listdir
from os.path import isfile, join

# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=8080 --user-data-dir="C:\Users\Zanshin\Documents\chromeprofile"

# Abrindo o Chrome no modo de debugging e acessando o Whatsapp Web

options = Options()
options.add_experimental_option("debuggerAddress","localhost:8080")
driver = webdriver.Chrome(options)
driver.get("https://web.whatsapp.com/")

# Clicka na primeira conversa da lista, abre as figurinhas e clicka em 'Criar'

wait = WebDriverWait(driver, timeout=6)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak8l")))
driver.find_element(By.CSS_SELECTOR, "div._ak8l").click() # Dica: crie uma conversa com você mesmo e fixe no topo para mandar as figurinhas para você mesmo
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.x10l6tqk")))
driver.find_element(By.CSS_SELECTOR, ".x1vpptot:nth-child(2) span").click()
driver.find_element(By.CSS_SELECTOR, ".x10l6tqk:nth-child(4) > div > span").click()


# Pegando todos os arquivos da pasta especificada

path = "C:\\Users\\Zanshin\\Pictures\\dbz"

dbzImages = [f for f in listdir(path) if isfile(join(path, f))]

# Fazendo e enviando as figurinhas

for img in dbzImages:

    driver.find_element(By.CSS_SELECTOR, ".x1lraqik").click()

    time.sleep(1)

    keyboard = Controller()

    keyboard.type(path + "\\" + img)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._ajv7:nth-child(7) > ._ajv6 > span")))
    driver.find_element(By.CSS_SELECTOR, "._ajv7:nth-child(7) > ._ajv6 > span").click()
    pyautogui.moveTo(778, 265, duration=0.2)
    keyboard.press(Key.alt)
    pyautogui.dragTo(789,285, duration=0.2)
    keyboard.release(Key.alt)
    driver.find_element(By.CSS_SELECTOR, ".x1rluvsa").click()



