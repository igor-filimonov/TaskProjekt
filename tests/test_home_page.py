#  pytest -v --driver Chrome test_home_page.py
# python3 -m pytest -v --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_home_page.py
# pytest -s -v --tb=line --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_home_page.py


import pytest
from termcolor import colored

from pages.home_page import *


@pytest.mark.smoke
def test_open_home_page(web_browser):
    # """проверяет открытиу главной страницы сайта"""
    page = HomePage(web_browser)        # открываем главную страницу

    assert page.get_current_url() == 'https://arsenal-ekb.com/'     # сравниваем адрес открывшейся страницы с заданным


@pytest.mark.regression
def test_home_pages_write_whatsapp(web_browser):
    # проверяет работу логотипа 'whatsapp' в шапке сайта
    page = HomePage(web_browser)
    new_url = page.write_whatsapp.get_attribute('href')
    page.get(new_url)
    url = page.get_current_url()

    assert url == 'https://api.whatsapp.com/send/?phone=%2B79292222432&text&type=phone_number&app_absent=0'


@pytest.mark.regression
def test_home_pages_write_telegram(web_browser):
    # проверяет работу логотипа 'telegram' в шапке сайта
    page = HomePage(web_browser)  # открываем главную страницу
    new_url = page.write_telegram.get_attribute('href')
    page.get(new_url)
    url = page.get_current_url()

    assert new_url == url


@pytest.mark.regression
def test_home_pages_search_button(web_browser, search_input):
    # проверяет работу кнопки поиска в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.magnifying_glass.click()                   # нажимаем на "лупу" для активации строки поиска
    page.search_input = search_input                # вводим данные в поле поиска
    page.search_button.click()                      # нажимаем на "лупу"

    assert page.search_results.get_text() == search_input


@pytest.mark.regression
def test_home_pages_menu_in_header_catalog(web_browser):
    # проверяет работу кнопки 'Каталог' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_catalog.click()                  # Находим пункт меню "Каталог" и кликаем по нему

    assert page.menu_results.get_text() == 'Каталог'


@pytest.mark.regression
def test_home_pages_menu_in_header_new(web_browser):
    # проверяет работу кнопки 'Новости' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_news.click()                     # Находим пункт меню "Новости" и кликаем по нему

    assert page.menu_results.get_text() == 'Новости'


@pytest.mark.regression
def test_home_pages_menu_in_header_about(web_browser):
    # проверяет работу кнопки 'О магазине' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_about.click()                    # Находим пункт меню "О магазине" и кликаем по нему

    assert page.menu_results.get_text() == 'О магазине'


@pytest.mark.regression
def test_home_pages_menu_in_header_payment(web_browser):
    # проверяет работу кнопки 'Оплата, доставка и возврат' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_payment.click()               # Находим пункт меню "Оплата, доставка и возврат" и кликаем по нему

    assert page.menu_results.get_text() == 'Оплата, доставка и возврат'


@pytest.mark.regression
def test_home_pages_menu_in_header_info(web_browser):
    # проверяет работу кнопки 'Полезная информация' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_info.click()                     # Находим пункт меню "Полезная информация" и кликаем по нему

    assert page.menu_results.get_text() == 'Полезная информация'


@pytest.mark.regression
def test_home_pages_basket_number(web_browser):
    # проверяет работу кнопки 'Цифра около корзины' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.basket_number.click()                      # Находим кнопки 'Цифра около корзины' и кликаем по нему

    assert page.basket_results.get_text() == "Корзина пуста"


@pytest.mark.regression
def test_home_pages_menu_in_header_contacts(web_browser):
    # проверяет работу кнопки 'Контакты' в шапке сайти
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_contacts.click()                 # Находим пункт меню "Полезная информация" и кликаем по нему

    assert page.menu_results.get_text() == 'Контакты'


@pytest.mark.regression
def test_home_pages_menu_in_header_input(web_browser):
    page = HomePage(web_browser)                    # открываем главную страницу
    page.menu_item_input.click()                    # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')       # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')       # вводим валидный пароль
    page.menu_item_input_button.click()             # кликаем кнопку "Ок"

    menu_text = str(page.cabinet_answer.get_text())
    print(colored(menu_text, 'yellow'))
    header_text = str(page.header_answer.get_text())
    print(colored(header_text, 'yellow'))
    assert menu_text in "Личный кабинет" and header_text in "Мои заказы"


@pytest.mark.regression
def test_home_pages_menu_in_header_input_registration(web_browser):
    page = HomePage(web_browser)                        # открываем главную страницу
    page.menu_item_input.click()                        # кликаем по кнопке "Вход"
    page.menu_item_input_registration.click()           # кликаем по ссылке "Регистрация"

    assert page.menu_item_input_registration_result.get_text() == "Регистрация"


@pytest.mark.regression
def test_home_pages_menu_in_header_input_forgot_password(web_browser):
    page = HomePage(web_browser)                        # открываем главную страницу
    page.menu_item_input.click()                        # кликаем по кнопке "Вход"
    page.menu_item_input_forgot_password.click()        #

    assert page.menu_item_input_forgot_password_result.get_text() == "Восстановление пароля"


@pytest.mark.regression
def test_home_pages_menu_footer_catalog(web_browser):
    # проверяет работу кнопки 'Каталог' в подвале сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_footer_catalog.click()  # Находим пункт меню "Каталог" и кликаем по нему

    assert page.menu_results.get_text() == 'Каталог'


@pytest.mark.regression
def test_home_pages_menu_footer_new(web_browser):
    # проверяет работу кнопки 'Новости' в подвале сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_footer_news.click()  # Находим пункт меню "Новости" и кликаем по нему

    assert page.menu_results.get_text() == 'Новости'


@pytest.mark.regression
def test_home_pages_menu_footer_about(web_browser):
    # проверяет работу кнопки 'О магазине' в подвале сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_footer_about.click()  # Находим пункт меню "О магазине" и кликаем по нему

    assert page.menu_results.get_text() == 'О магазине'


@pytest.mark.regression
def test_home_pages_menu_footer_payment(web_browser):
    # проверяет работу кнопки 'Оплата, доставка и возврат' в подвале сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_footer_payment.click()  # Находим пункт меню "Оплата, доставка и возврат" и кликаем по нему

    assert page.menu_results.get_text() == 'Оплата, доставка и возврат'


@pytest.mark.regression
def test_home_pages_menu_footer_info(web_browser):
    # проверяет работу кнопки 'Полезная информация' в подвале сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_footer_info.click()  # Находим пункт меню "Полезная информация" и кликаем по нему

    assert page.menu_results.get_text() == 'Полезная информация'


@pytest.mark.regression
def test_home_pages_menu_footer_development(web_browser):
    # проверяет работу логотипа разработчиков в подвале сайти

    page = HomePage(web_browser)                    # открываем главную страницу
    new_url = page.menu_footer_development.get_attribute('href')
    page.get(new_url)
    url = page.get_current_url()
    assert url == 'https://apri-code.ru/'


@pytest.mark.regression
def test_home_pages_menu_body_weapon(web_browser):
    # проверяет работу кнопки 'Оружие' в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_weapon.click()  # Находим пункт меню "Оружие" и кликаем по нему

    assert page.menu_body_results.get_text() == "Оружие"


@pytest.mark.regression
def test_home_pages_menu_body_cartridges(web_browser):
    # проверяет работу кнопки 'Патроны' в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_cartridges.click()  # Находим пункт меню "Патроны" и кликаем по нему

    assert page.menu_body_results.get_text() == "Патроны"


@pytest.mark.regression
def test_home_pages_menu_body_optical(web_browser):
    # проверяет работу кнопки "Оптические прицелы в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_optical.click()  # Находим пункт меню "Оптические прицелы" и кликаем по нему

    assert page.menu_body_results.get_text() == 'Оптика'


@pytest.mark.regression
def test_home_pages_menu_body_crossbows(web_browser):
    # проверяет работу кнопки "Луки, арбалеты" в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_crossbows.click()  # Находим пункт меню "Луки, арбалеты" и кликаем по нему

    assert page.menu_body_results.get_text() == "Луки, Арбалеты"


@pytest.mark.regression
def test_home_pages_menu_body_safes(web_browser):
    # проверяет работу кнопки "Шкафы и оружейные сейфы" в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_safes.click()  # Находим пункт меню "Шкафы и оружейные сейфы" и кликаем по нему

    assert page.menu_body_results.get_text() == "Сейфы оружейные"


@pytest.mark.regression
def test_home_pages_menu_body_gift(web_browser):
    # проверяет работу кнопки "варианты для подарков" в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_gift.click()  # Находим пункт меню "варианты для подарков" и кликаем по нему

    assert page.menu_body_results.get_text() == "В подарок"


@pytest.mark.regression
def test_home_pages_menu_body_clothes(web_browser):
    # проверяет работу кнопки "Охотничья одежда и обувь" в теле сайти
    page = HomePage(web_browser)  # открываем главную страницу
    page.menu_body_clothes.click()  # Находим пункт меню "Охотничья одежда и обувь" и кликаем по нему

    assert page.menu_body_results.get_text() == "Remington"
