from time import sleep
import sys
import adshopcart_locators as locators
from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Open Web Browser
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Navigate to Advantage Shopping web page
def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get('https://advantageonlineshopping.com/')
    if driver.current_url == locators.adshopcart_url and driver.title == driver.title:
        sleep(2)
        print(f'Test Started at: {datetime.datetime.now()}')
        print(f'We are at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- {driver.title}')
        print(f'Welcome to Advantage Online Shopping Website.')
        print(f'-------------------------------------------')
    else:
        print(f'We\'re not at the Advantage Shopping homepage.Try again')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'-------------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
        sleep(1)


setUp()
tearDown()

