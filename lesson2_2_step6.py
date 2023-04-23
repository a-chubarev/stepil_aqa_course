from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import log
import math


def return_math_result(first_arg):
    return log(abs(12*math.sin(int(first_arg))))

browser = webdriver.Chrome()
browser.get('https://SunInJuly.github.io/execute_script.html')

try:
    math_arg = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    print(math_arg)
    math_result = return_math_result(math_arg)
    print(math_result)

    result_field = browser.find_element(By.XPATH, '//input[@id="answer"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", result_field)
    result_field.send_keys(f'{math_result}')

    capcha_checkbox = browser.find_element(By.XPATH, '//input[@id="robotCheckbox" and @type="checkbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", capcha_checkbox)
    capcha_checkbox.click()

    capcha_radiobutton = browser.find_element(By.XPATH, '//input[@value="robots" and @type="radio"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", capcha_radiobutton)
    capcha_radiobutton.click()

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit" and text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
