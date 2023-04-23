import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait




browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
browser.implicitly_wait(5)

try:
    #Выбираем нужную цену
    price = WebDriverWait(browser, 20).until(expected_conditions.text_to_be_present_in_element(
                                            (By.XPATH, '//h5[@id="price"]'),'$100'))
    browser.find_element(By.XPATH, '//button[@id="book"]').click()

    #Решаем вторую задачу
    math_arg = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    result = math.log(abs(12*math.sin(int(math_arg))))
    browser.find_element(By.XPATH, '//input[@name="text"]').send_keys(result)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()