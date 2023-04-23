from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/math.html'

def math_answer(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.XPATH, '//input[@class="form-control"]').send_keys(f'{math_answer(x)}')

    browser.find_element(By.XPATH, '//input[@type="checkbox"]').click()

    browser.find_element(By.XPATH, '//input[@type="radio" and @value="robots"]').click()

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(5)
    browser.quit()