#  pytest -v --driver Chrome test_cabinet_page.py
# python3 -m pytest -v --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_cabinet_page.py
# pytest -s -v --tb=line --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_cabinet_page.py

import pytest
from termcolor import colored

from pages.cabinet_page import *


@pytest.mark.smoke
@pytest.mark.regression
def test_input_personal_cabinet(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()

    menu_text = str(page.cabinet_answer.get_text())
    print(colored(menu_text, 'yellow'))
    header_text = str(page.header_answer.get_text())
    print(colored(header_text, 'yellow'))
    assert menu_text in "Личный кабинет" and header_text in "Мои заказы"


@pytest.mark.smoke
@pytest.mark.regression
def test_input_cabinet_messages(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в меню сообщения в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.messages.click()

    menu_text = str(page.cabinet_answer.get_text())
    print(colored(menu_text, 'yellow'))
    header_text = str(page.header_answer.get_text())
    print(colored(header_text, 'yellow'))
    assert menu_text in "Личный кабинет" and header_text in "Сообщения"


@pytest.mark.skip   # поставил skip что бы не напрягать манагеров сайт действующий
def test_cabinet_send_messages_manager(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в меню сообщения в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.messages.click()

    page.input_messages.send_keys('Привет!')        # пишем сообщение менеджеру из личного кабинета
    page.button_messages.click()                    # отправляем сообщение

    # assert -- проверить нельзя т.к. нет доступа к почте сайта


@pytest.mark.regression
def test_cabinet_personal_data(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()

    menu_text = str(page.cabinet_answer.get_text())
    print(colored(menu_text, 'yellow'))
    header_text = str(page.header_answer.get_text())
    print(colored(header_text, 'yellow'))
    assert menu_text in "Личный кабинет" and header_text in "Личные данные"


@pytest.mark.regression
def test_cabinet_personal_data_edit_open(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()
    # переходим в меню "Редактировать"
    page.menu_edit.click()

    menu_text = str(page.edit_answer.get_text())
    print(colored(menu_text, 'yellow'))

    assert menu_text in "Личные данные"


@pytest.mark.regression
def test_cabinet_personal_data_add_address_open(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()
    # переходим в меню "Добавить адрес"
    page.menu_add_address.click()

    menu_text = str(page.add_answer.get_text())
    print(colored(menu_text, 'yellow'))

    assert menu_text in "Добавить адрес"


@pytest.mark.regression
def test_input_cabinet_personal_data_add_address_open(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()
    # переходим в меню "Сменить пароль"
    page.menu_change_password.click()

    menu_text = str(page.add_answer.get_text())
    print(colored(menu_text, 'yellow'))

    assert menu_text in "Смена пароля"


@pytest.mark.regression
def test_input_cabinet_personal_data_edit(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()
    # переходим в меню "Редактировать"
    page.menu_edit.click()
    # редактируем данные
    page.edit_i_name.send_keys('Владимир')
    page.edit_f_name.send_keys('Умников')
    page.edit_o_name.send_keys('Николаевич')
    page.edit_email.send_keys('44942@hghgjh.com')
    page.edit_phone.send_keys('9873980022')
    page.edit_button.click()

    menu_text = str(page.sms.get_text())
    print(colored(menu_text, 'yellow'))

    assert menu_text in "Данные сохранены"


@pytest.mark.regression
def test_input_cabinet_personal_data_add_address(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    # переходит на вкладку "Добавить адрес", вводим данные, отправляем
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()
    # переходим в меню "Добавить адрес"
    page.menu_add_address.click()

    page.add_city.send_keys('Москва')
    page.add_index.send_keys('000000')
    page.add_street.send_keys('Тверская')
    page.add_house.send_keys('31')
    page.add_room.send_keys('2')
    page.add_button.click()

    menu_text = str(page.sms.get_text())
    print(colored(menu_text, 'yellow'))

    assert menu_text in "Данные сохранены"


@pytest.mark.regression
def test_cabinet_personal_data_clear_address(web_browser):
    # Тест заходит на главную страницу, вводит данные пользователя и переходит в личный кабинет
    # переходит на вкладку "Добавить адрес", вводим данные, отправляем
    page = CabinetPage(web_browser)  # открываем главную страницу
    page.menu_item_input.click()  # кликаем по кнопке "Вход"
    page.menu_item_input_username.send_keys('44942@hghgjh.com')  # вводим валидный логин
    page.menu_item_input_password.send_keys('123456789')  # вводим валидный пароль
    page.menu_item_input_button.click()  # кликаем кнопку "Ок"
    page.cabinet.click()
    # переходим в меню "Личные данные"
    page.menu_personal_data.click()
    # переходим в меню "Редактировать адрес"
    page.edit_address.click()
    page.clear_address.click()

    menu_text = str(page.sms.get_text())
    print(colored(menu_text, 'yellow'))

    assert menu_text in "Адрес удален"
