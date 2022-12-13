import pytest
from selenium import webdriver
import random
from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def creating_valid_name():
    return {'name':'Sergey', 'email':('sergeykravchenko5_'+str(random.randint(100, 999))+'@yandex.ru'), 'password': str(random.randint(100000, 999999))}

@pytest.fixture()
def driver():
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome() #chrome_options=chrome_options
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture()
def account_this_incorrected_password():
    return {'email': 'sss@yandex.ru', 'password': str(random.randint(10000, 99999))}

@pytest.fixture()
def registered_account():
    return {'email': 'www@ya.ru', 'password': '123456'}

@pytest.fixture()
def driver_and_login(registered_account):
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome() #chrome_options=chrome_options
    driver.get('https://stellarburgers.nomoreparties.site/')
    email_for_login = registered_account.get('email')
    password_for_login = registered_account.get('password')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_LOG_IN)))
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN).click()
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_ON_ENTRANCE).send_keys(email_for_login)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_ON_ENTRANCE).send_keys(password_for_login)
    driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).click()
    yield driver
    driver.quit()