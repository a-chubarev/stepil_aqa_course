import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
time.sleep(10)

driver.get('https://suninjuly.github.io/text_input_task.html')
find_text =  driver.find_element(By.CSS_SELECTOR, '.textarea')

find_text.send_keys("get()")
time.sleep(15)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()
time.sleep(10)


driver.quit()