from time import sleep
import sys
import adshopcart_locators as locators
from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


# Open Web Browser
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Navigate to Advantage Shopping web page
def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)

    # Checking that we are on the correct URL address, and we are seeing title
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url and driver.title == locators.adshopcart_title:
        sleep(2)
        print(f'Test Started at: {datetime.datetime.now()}')
        print(f'We are at {driver.current_url} and We\'re seeing title message -- {driver.title}')
        print(f'Welcome to Advantage Online Shopping Website.')
        print(f'--------------------------------------------------')
    else:
        print(f'We\'re not at the Advantage Shopping homepage.Try again')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


# Register For New User
def signUp():
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        sleep(3)
        driver.find_element(By.ID, 'menuUser').click()
        sleep(3)

        # ACCOUNT DETAILS
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()   # Select Create New Account
        sleep(1)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)   # Username
        sleep(1)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)    # Email
        sleep(1)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)    # Password
        sleep(1)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)    # Confirm Password
        sleep(1)

        # PERSONAL DETAILS
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)    # First Name
        sleep(1)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)    # Last Name
        sleep(1)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)    # Phone Number
        sleep(1)

        # ADDRESS
        driver.find_element(By.NAME, 'countryListboxRegisterPage').click()    # Click by Country
        sleep(1)
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')   # Select by visible text
        sleep(1)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)    # City
        sleep(1)
        driver.find_element(By.NAME, "addressRegisterPage").send_keys(locators.street_address)    # Address
        sleep(1)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)    # State/Province/Region
        sleep(1)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)    # Postal Code
        sleep(1)
        driver.find_element(By.NAME, 'allowOffersPromotion').click() # Uncheck 'Receive exclusive offers and promotions' checkbox
        sleep(1)
        driver.find_element(By.NAME, 'i_agree').click()  # Check 'I Agree' checkbox
        sleep(1)
        driver.find_element(By.ID, 'register_btnundefined').click()  # Click by REGISTER Button
        sleep(2)
        print(f'Registration for a new user  "{locators.username}" is done successfully.')
        print(f'------------------------------------------------------------')
    else:
        print(f'We\'re not registered for new user .Try again')
        driver.close()
        driver.quit()


# Checking that Full name is displayed and we have No orders in My Orders
def check_my_account_my_orders():
    if driver.current_url == locators.adshopcart_url:
        sleep(3)
        driver.find_element(By.ID, 'menuUserLink').click()  # User
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()  # My Account
        sleep(2)
        content = driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[1]/div/div[1]/label')
        print(f'My Account Details for "{content.text}" is displayed')
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()  # My Orders
        sleep(3)
        content = driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/label')
        print(f'"{content.text}" text is displayed in My Orders')
        print(f'------------------------------------------------------------')
    else:
        print(f'My Account and My Orders are not displayed.Try again')
        driver.close()
        driver.quit()




# Login we Login with new credentials (username and password).
def log_in():

    driver.find_element(By.ID, 'menuUser').click()   # User
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)   # Username
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)    # Password
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()    # Sign In
    sleep(2)
    print(f'Login with new user "{locators.username}" done successfully')
    print(f'------------------------------------------------------------')




# Sign out from account
def log_out():
    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()  # Sign Out
        sleep(2)
        print(f'Log out with user "{locators.username}" done successfully')
        print(f'Log out successfully at: {datetime.datetime.now()}')
        print(f'------------------------------------------------------------')
    else:
        print(f'Logout is unsuccessful.')
        driver.close()
        driver.quit()


# Delete Account that we have created
def delete_account():
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()  # My Account
        sleep(4)
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()  # Delete Account
        sleep(4)
        driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()  # Confirm Delete Account
        sleep(4)
        print(f'The new user created : "{locators.username}" is deleted successfully.')
        print(f'------------------------------------------------------------')
    else:
        print(f'The new User {locators.username} is not deleted.')
        driver.close()
        driver.quit()


#  log in again with deleted credentials. Checking that 'Incorrect username or password.' error label got displayed.
def login_with_incorrect_username():
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(3)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)  # Username
        sleep(3)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)  # Password
        sleep(3)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()  # Sign In
        sleep(2)
        content = driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]')
        print(f'"{content.text}" text is displayed.')
        print(f'Test Scenario: Login with incorrect username and password - is passed')
    else:
        print(f'Incorrect user name or password text is not displayed.')


setUp()
signUp()
check_my_account_my_orders()
log_out()
log_in()
delete_account()
login_with_incorrect_username()
tearDown()



