class locators:
    BUTTON_LOG_IN = '//*[text()="Войти в аккаунт"]' #Кнопка войти на главной странице
    BUTTON_REGISTRATION_IN_LOG_IN = '//*[text()="Зарегистрироваться"]' #Кнопка зарегистрироваться на странице входа
    NAME_FIELD_IN_REGISTRATION = '(//*[@class="text input__textfield text_type_main-default"])[1]' #Поле ввода имени на странице регистрации
    EMAIL_FIELD_IN_REGISTRATION = '(//*[@class="text input__textfield text_type_main-default"])[2]' #Поле емейла на странице регистрации
    PASSWORD_FIELD_IN_REGISTRATION = '//input[@name="Пароль"]' #Поле пароля на странице регистрации
    BUTTON_REGISTRATION = '//*[text()="Зарегистрироваться"]' #Кнопка зарегистрироваться на странице регистрации
    BUTTON_LOG_IN_ON_REGISTRATION = '//*[text()="Войти"]' #Кнопка войти на странице регистрации
    EMAIL_FIELD_ON_ENTRANCE = '(//*[@class="text input__textfield text_type_main-default"])[1]' #Поле емейла на странице входа
    PASSWORD_FIELD_ON_ENTRANCE = '(//*[@class="text input__textfield text_type_main-default"])[2]' #Поле пароля на странице входа
    BUTTON_ON_ENTRANCE = '//*[text()="Войти"]' #Кнопка войти на странице входа
    BUTTON_PLACE_AN_ORDER = '//*[text()= "Оформить заказ"]' #Кнопка оформить заказ на главной после авторизации
    BUTTON_FORGOT_PASSWORD = '//*[text()="Восстановить пароль"]' #Кнопка восстановить пароль на странице входа
    BUTTON_LOG_IN_ON_FORGOT_PASSWORD = '//*[text()="Войти"]' #Кнопка вход на странице восстановления пароля
    BUTTON_YOUR_PERSONAL_ACCOUNT = '(//*[@class="AppHeader_header__linkText__3q_va ml-2"])[3]' #Кнопка личного кабинета
    BUTTON_SAVE_ON_PERSONAL_DATA = '//*[text()="Сохранить"]' #Кнопка сохранить в личном кабинете
    BUTTON_CONSTRUCTOR = '//*[text()="Конструктор"]' #Кнопка конструктор
    BUTTON_STELLAR_BURGERS = '//*[@class="AppHeader_header__logo__2D0X2"]' #Кнопка Stellar Burgers
    BUTTON_LOG_OUT = '//*[text()="Выход"]' #Кнопка выхода в личном кабинете
    BUTTON_SAUSES = '//*[contains(@class, "tab_tab__1SPyG")][2]' #Кнопка соусы
    BUTTON_BREAD = '//*[contains(@class, "tab_tab__1SPyG")][1]' #Кнопка булки
    BUTTON_FILLINGS = '//*[contains(@class, "tab_tab__1SPyG")][3]' #Кнопка начинки
    INCORRECTED_PASSWORD = '//*[@class="input__error text_type_main-default"]' #Надпись некоректного пароля

