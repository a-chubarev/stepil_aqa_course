from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    browser.switch_to.alert.accept()

    math_arg = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    result = math.log(abs(12*math.sin(int(math_arg))))

    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()