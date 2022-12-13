from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_main_page_login_on_button_login_to_account(driver,registered_account): #вход по кнопке «Войти в аккаунт» на главной
    email_for_login = registered_account.get('email')
    password_for_login = registered_account.get('password')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_LOG_IN)))
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN).click()
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_ON_ENTRANCE).send_keys(email_for_login)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_ON_ENTRANCE).send_keys(password_for_login)
    driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_PLACE_AN_ORDER)))
    place_order = driver.find_element(By.XPATH, locators.BUTTON_PLACE_AN_ORDER).text
    place = "Оформить заказ"
    assert place_order == place

def test_login_your_personal_account(driver, registered_account): #вход через кнопку «Личный кабинет»
    email_for_login = registered_account.get('email')
    password_for_login = registered_account.get('password')
    driver.find_element(By.XPATH, locators.BUTTON_YOUR_PERSONAL_ACCOUNT).click()
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_ON_ENTRANCE).send_keys(email_for_login)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_ON_ENTRANCE).send_keys(password_for_login)
    driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_PLACE_AN_ORDER)))
    place_order = driver.find_element(By.XPATH, locators.BUTTON_PLACE_AN_ORDER).text
    place = "Оформить заказ"
    assert place_order == place

def test_login_button_in_registration_form(driver, registered_account): #вход через кнопку в форме регистрации
    email_for_login = registered_account.get('email')
    password_for_login = registered_account.get('password')
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN).click()
    driver.find_element(By.XPATH, locators.BUTTON_REGISTRATION_IN_LOG_IN)
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN_ON_REGISTRATION)
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_ON_ENTRANCE).send_keys(email_for_login)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_ON_ENTRANCE).send_keys(password_for_login)
    driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_PLACE_AN_ORDER)))
    place_order = driver.find_element(By.XPATH, locators.BUTTON_PLACE_AN_ORDER).text
    place = "Оформить заказ"
    assert place_order == place

def test_login_button_in_password_recovery_form(driver, registered_account): #вход через кнопку в форме восстановления пароля
    email_for_login = registered_account.get('email')
    password_for_login = registered_account.get('password')
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN).click()
    driver.find_element(By.XPATH, locators.BUTTON_FORGOT_PASSWORD)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_LOG_IN_ON_FORGOT_PASSWORD)))
    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN_ON_FORGOT_PASSWORD)
    driver.find_element(By.XPATH, locators.EMAIL_FIELD_ON_ENTRANCE).send_keys(email_for_login)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD_ON_ENTRANCE).send_keys(password_for_login)
    driver.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_PLACE_AN_ORDER)))
    place_order = driver.find_element(By.XPATH, locators.BUTTON_PLACE_AN_ORDER).text
    place = "Оформить заказ"
    assert place_order == place
