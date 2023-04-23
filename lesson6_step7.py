from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser.get(link)

    input_fields = browser.find_elements(By.CSS_SELECTOR, '[type = "text"]')
    print(input_fields)
    for text_block in input_fields:
        text_block.send_keys(f'{random.randint(0,10)}')

    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()


finally:
    time.sleep(30)
    browser.quit()