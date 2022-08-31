# pytest -v --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_registrasion_page.py
# pytest -s -v --tb=line --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_registrasion_page.py
# pytest -s -v -m proba --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_registrasion_page.py


import pytest
from termcolor import colored

from pages.registrasion_page import *


@pytest.mark.smoke
def test_open_registrasion_page(web_browser):
    # проверяет открытиe главной страницы сайта
    page = RegistrasionPage(web_browser)  # открываем главную страницу
    # сравниваем адрес открывшейся страницы с заданным
    assert page.get_current_url() == 'https://arsenal-ekb.com/registration'


@pytest.mark.skip
@pytest.mark.smoke
def test_registrasion_new_user_validation(web_browser):
    # проверяет работу формы регистрации с валидными данными
    page = RegistrasionPage(web_browser)  # Открываем страницу регистрации
    page.email.send_keys('44942@hghgjh.com')  # в поле "email*" записываем валидный email
    page.password1.send_keys('123456789')  # в поле "Пароль*" записываем валидный пароль
    page.password2.send_keys('123456789')  # в поле "Подтверждение*" записываем валидный пароль
    page.name1.send_keys('Иванович')  # в поле "Фамилия*" записываем валидные данные
    page.name2.send_keys('Павел')  # в поле "Имя*" записываем валидные данные
    page.phone.send_keys('9871239800')  # в поле "Телефон*" записываем валидные данные
    page.box.click()  # кликаем на "чекбокс" - "Согласен на обработку данных"
    page.button.click()  # кликаем на кнопку - "зарегистрироваться"

    assert "Форма успешно отправлена." in page.answer1.get_text()


@pytest.mark.regression
@pytest.mark.invalid
def test_registrasion_new_user_validation_repeat_email(web_browser, email='942@hghgjh.com'):
    # проверяет работу формы регистрации с повторной попыткой регистрации по одному email
    page = RegistrasionPage(web_browser)  # Открываем страницу регистрации
    page.email.send_keys(email)  # в поле "email*" записываем валидный email
    page.password1.send_keys('123456789')  # в поле "Пароль*" записываем валидный пароль
    page.password2.send_keys('123456789')  # в поле "Подтверждение*" записываем валидный пароль
    page.name1.send_keys('Иванович')  # в поле "Фамилия*" записываем валидные данные
    page.name2.send_keys('Павел')  # в поле "Имя*" записываем валидные данные
    page.phone.send_keys('9991112201')  # в поле "Телефон*" записываем валидные данные
    page.box.click()  # кликаем на "чекбокс" - "Согласен на обработку данных"
    page.button.click()  # кликаем на кнопку - "зарегистрироваться"
    menu_text = str(page.answer2.get_text())
    print(colored(menu_text, 'yellow'))

    assert 'Логин' and email and 'уже занят' in menu_text


@pytest.mark.regression
@pytest.mark.invalid
@pytest.mark.parametrize(
    ('email', 'password1', 'password2', 'name1', 'name2', 'phone', 'answer'),
    [
        ('', '', '', '', '', '9991112200', 'Необходимо заполнить поле E-mail.' and 'Необходимо заполнить поле Фамилия.'
         and 'Необходимо заполнить поле Имя.' and 'Необходимо заполнить поле Подтвеждение.'
         and 'Необходимо заполнить поле Пароль.'),
        ('9991112200@hghgjh.com', '', '', '', '', '9991112200', 'Необходимо заполнить поле Пароль.'
         and 'Необходимо заполнить поле Подтвеждение.' and 'Необходимо заполнить поле Фамилия.'
         and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', 'фывапр', '', '', '', '9991112200', 'Необходимо заполнить поле Подтвеждение.'
         and 'Необходимо заполнить поле Фамилия.' and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', '', 'фывапр', '', '', '9991112200', 'Необходимо заполнить поле Пароль.'
         and 'Необходимо заполнить поле Фамилия.' and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', '', '', 'Smit', '', '9991112200', 'Необходимо заполнить поле Пароль.'
         and 'Необходимо заполнить поле Подтвеждение.' and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', '', '', '', 'Ted', '9991112200', 'Необходимо заполнить поле Пароль.'
         and 'Необходимо заполнить поле Подтвеждение.' and 'Необходимо заполнить поле Фамилия.'),
        ('', '123456', '123456', '', '', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Фамилия.' and 'Необходимо заполнить поле Имя.'),
        ('', '123456', '', 'Иванов', '', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Подтвеждение.' and 'Необходимо заполнить поле Имя.'),
        ('', '123456', '', '', 'Петр', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Подтвеждение.' and 'Необходимо заполнить поле Фамилия.'),
        ('', '', 'оррп;:343', '', 'Петр', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Пароль.' and 'Необходимо заполнить поле Фамилия.'),
        ('', '', '', '345&^^%$', 'Петр', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Подтвеждение.' and 'Необходимо заполнить поле Пароль.'),
        ('', '', '9876%:??*', '', 'Петр', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Пароль.' and 'Необходимо заполнить поле Фамилия.'),
        ('9991112200@hghgjh.com', 'qwerty', 'qwerty', '', '', '9991112200', 'Необходимо заполнить поле Фамилия.'
         and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', 'qwerty', 'qwerty', '123456', '', '9991112200', 'Необходимо заполнить поле Имя.'),
        ('', 'qwerty', 'qwerty', '123456', '', '9991112200', 'Необходимо заполнить поле E-mail.'
         and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', '', 'qwerty', '123456', '', '9991112200', 'Необходимо заполнить поле Пароль.'
         and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', 'qwerty', '', '123456', '', '9991112200', 'Необходимо заполнить поле Подтвеждение.'
         and 'Необходимо заполнить поле Имя.'),
        ('9991112200@hghgjh.com', 'qwerty', 'йцукен', '123456', '123', '9991112200',
         "Пароль и подтверждение должны совпадать"),
    ],
)
def test_registrasion_new_user_invalid_data(web_browser, email, password1, password2, name1, name2, phone, answer):
    # проверяет обработку ошибок в форме регистрации
    page = RegistrasionPage(web_browser)  # открываем главную страницу
    page.email.send_keys(email)
    page.password1.send_keys(password1)
    page.password2.send_keys(password2)
    page.name1.send_keys(name1)
    page.name2.send_keys(name2)
    page.phone.send_keys(phone)
    page.box.click()
    page.button.click()
    menu_text = page.answer2.get_text()
    print(colored(menu_text, 'yellow'))

    assert answer in menu_text


@pytest.mark.regression
@pytest.mark.invalid
@pytest.mark.parametrize(
    ('phone', 'answer'),
    [
        ('', "Проверьте правильность введенного телефона"),
        ('9991', "Проверьте правильность введенного телефона"),
        ('ыо12bd%$', "Проверьте правильность введенного телефона"),
    ],
)
def test_registrasion_new_user_invalid_data_phone(web_browser, phone, answer):
    # проверяет обработку ошибок в форме регистрации
    page = RegistrasionPage(web_browser)  # открываем главную страницу
    page.phone.send_keys(phone)
    page.box.click()
    page.button.click()
    menu_text = page.sms_error_phone.get_text()
    print(colored(menu_text, 'yellow'))

    assert answer in menu_text


@pytest.mark.regression
@pytest.mark.invalid
def test_registrasion_new_user_invalid_checkbox(web_browser, answer="Необходимо дать согласие на обработку данных"):
    # проверяет обработку ошибок в форме регистрации checkbox
    page = RegistrasionPage(web_browser)  # открываем главную страницу
    page.email.send_keys("123@jhgjh.com")
    page.password1.send_keys("123")
    page.password2.send_keys("123")
    page.name1.send_keys("Sem")
    page.name2.send_keys("Smit")
    page.phone.send_keys("9879870021")
    # page.box.click()
    page.button.click()
    menu_text = page.answer2.get_text()
    print(colored(menu_text, 'yellow'))

    assert answer in menu_text
