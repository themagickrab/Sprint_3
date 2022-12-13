from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_successful_user_registration(driver, creating_valid_name): #Регистрация
    name_for_registration = creating_valid_name.get('name')
    email_for_registration = creating_valid_name.get('email')
    password_for_registration = creating_valid_name.get('password')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_LOG_IN)))
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN).click()
    driver.find_element(By.XPATH, locators.BUTTON_REGISTRATION_IN_LOG_IN)
    driver.find_element(By.XPATH, locators.NAME_FIELD_IN_REGISTRATION).send_keys(name_for_registration)
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_IN_REGISTRATION).send_keys(email_for_registration)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_IN_REGISTRATION).send_keys(password_for_registration)
    driver.find_element(By.XPATH, locators.BUTTON_REGISTRATION).click()
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN_ON_REGISTRATION).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_ON_ENTRANCE)))
    login_text = driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).text
    login = 'Войти'
    assert login_text == login

def test_error_for_incorrect_password(driver, account_this_incorrected_password): #Вход с не верным паролем
    email_for_login = account_this_incorrected_password.get('email')
    password_for_login = account_this_incorrected_password.get('password')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_LOG_IN)))
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN).click()
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_ON_ENTRANCE).send_keys(email_for_login)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_ON_ENTRANCE).send_keys(password_for_login)
    driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).click()
    incorrected_password = driver.find_element(By.XPATH, locators.INCORRECTED_PASSWORD).text
    assert incorrected_password == 'Некорректный пароль'
