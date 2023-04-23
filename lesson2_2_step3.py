from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def return_math_action(first_arg, second_arg):
    return int(first_arg) + int(second_arg)

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects2.html')

try:
    first_argument = browser.find_element(By.XPATH, '//span[@id="num1"]').text
    second_argument = browser.find_element(By.XPATH, '//span[@id="num2"]').text

    result = return_math_action(first_argument, second_argument)
    print(result)

    result_dropdown = Select(browser.find_element(By.XPATH, '//select[@id="dropdown" and @class="custom-select"]'))
    result_dropdown.select_by_value(f'{result}')

    browser.find_element(By.XPATH, '//button[@type="submit" and text()="Submit"]').click()

finally:
    time.sleep(5)
    browser.quit()