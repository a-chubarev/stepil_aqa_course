from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/registration2.html'
successful_registration = 'Congratulations! You have successfully registered!'

try:
    browser.get(link)


    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    first_name.send_keys('Test Data')

    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    last_name.send_keys('Test Data')

    email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    email.send_keys('Test Data')

    registration_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    registration_button.click()

    time.sleep(5)

    welcome_text = browser.find_element(By.XPATH, '//h1').text
    assert welcome_text == successful_registration



finally:
    time.sleep(1)
    browser.quit()