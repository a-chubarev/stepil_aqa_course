from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


try:
    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Иванов')
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Иван')
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('ivanov@ivan.ivan')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    attach_file = os.path.join(current_dir, 'lesson2_2_step7.txt')

    browser.find_element(By.XPATH, '//input[@name="file"]').send_keys(attach_file)

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()