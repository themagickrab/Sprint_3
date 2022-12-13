from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_transfer_to_your_personal_account(driver_and_login): #Проверь переход по клику на «Личный кабинет»
    driver_and_login.find_element(By.XPATH, locators.BUTTON_YOUR_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUTTON_SAVE_ON_PERSONAL_DATA)))
    button_save = driver_and_login.find_element(By.XPATH, locators.BUTTON_SAVE_ON_PERSONAL_DATA).text
    save = 'Сохранить'
    assert button_save == save
