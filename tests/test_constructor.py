from locators_test import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_go_to_the_sauces_section(driver_and_login): #Клик по вкладке соус
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_SAUSES)))
    driver_and_login.find_element(By.XPATH, locators.BUTTON_SAUSES).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[text()="Соус традиционный галактический"]')))
    souses_text = driver_and_login.find_element(By.XPATH, '//*[text()="Соус традиционный галактический"]').text
    souses = 'Соус традиционный галактический'
    assert souses_text == souses

def test_go_to_the_bread_section(driver_and_login): #Клик по вкладке булки
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_SAUSES)))
    driver_and_login.find_element(By.XPATH, locators.BUTTON_SAUSES).click()
    driver_and_login.find_element(By.XPATH, locators.BUTTON_BREAD).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]')))
    bread_text = driver_and_login.find_element(By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]').text
    bread = 'Флюоресцентная булка R2-D3'
    assert bread_text == bread

def test_go_to_the_fillings_section(driver_and_login): #Клик по вкладке начинка
    WebDriverWait(driver_and_login, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.BUTTON_FILLINGS)))
    driver_and_login.find_element(By.XPATH, locators.BUTTON_FILLINGS).click()
    WebDriverWait(driver_and_login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="Филе Люминесцентного тетраодонтимформа"]')))
    fillings_text = driver_and_login.find_element(By.XPATH, '//*[text()="Филе Люминесцентного тетраодонтимформа"]').text
    fillings = 'Филе Люминесцентного тетраодонтимформа'
    assert fillings_text == fillings