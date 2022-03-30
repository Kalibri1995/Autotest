from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://yandex.ru/')
searchbox = driver.find_element(by=By.XPATH, value='//*[@id="text"]')
searchbox.send_keys('Тензор')

