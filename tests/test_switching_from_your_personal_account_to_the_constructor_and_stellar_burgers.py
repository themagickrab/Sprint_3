from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_switching_from_your_personal_account_to_the_constructor(driver_and_login): #переход по клику на «Конструктор»
    driver_and_login.find_element(By.XPATH, locators.BUTTON_YOUR_PERSONAL_ACCOUNT).click()
    driver_and_login.find_element(By.XPATH, locators.BUTTON_CONSTRUCTOR).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_PLACE_AN_ORDER)))
    place_order = driver_and_login.find_element(By.XPATH, locators.BUTTON_PLACE_AN_ORDER).text
    place = "Оформить заказ"
    assert place_order == place

def test_switching_from_your_personal_account_to_the_stella_burgers(driver_and_login): #переход по клику на логотип Stellar Burgers
    driver_and_login.find_element(By.XPATH, locators.BUTTON_YOUR_PERSONAL_ACCOUNT).click()
    driver_and_login.find_element(By.XPATH, locators.BUTTON_STELLAR_BURGERS).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_PLACE_AN_ORDER)))
    place_order = driver_and_login.find_element(By.XPATH, locators.BUTTON_PLACE_AN_ORDER).text
    place = "Оформить заказ"
    assert place_order == place