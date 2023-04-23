from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    math_arg = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    result = math.log(abs(12 * math.sin(int(math_arg))))

    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()
