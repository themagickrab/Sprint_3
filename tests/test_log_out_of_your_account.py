from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_log_out_of_your_account(driver_and_login): #Выход из аккаунта
    driver_and_login.find_element(By.XPATH, locators.BUTTON_YOUR_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_LOG_OUT)))
    driver_and_login.find_element(By.XPATH, locators.BUTTON_LOG_OUT).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_ON_ENTRANCE)))
    login = driver_and_login.find_element(By.XPATH, locators.BUTTON_ON_ENTRANCE).text
    login_text = 'Войти'
    assert login == login_text
