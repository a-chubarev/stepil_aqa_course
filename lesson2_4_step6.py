from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/cats.html')
browser.implicitly_wait(10)

browser.find_element(By.ID, "button")