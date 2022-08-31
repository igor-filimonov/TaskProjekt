#  pytest -v --driver Chrome test_home_page.py
# python3 -m pytest -v --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_catalog_page.py
# pytest -s -v --tb=line --driver Chrome --driver-path /home/igor/Загрузки/chromedriver test_catalog_page.py
import pytest
from pages.catalog_page import *


@pytest.mark.regression
def test_open_home_page(web_browser):
    # проверяет открытиe главной страницы сайта
    page = CatalogPage(web_browser)  # открываем главную страницу
    # сравниваем адрес открывшейся страницы с заданным
    assert page.get_current_url() == 'https://arsenal-ekb.com/catalogue/podarochnye-sertifikaty'


@pytest.mark.regression
def test_catalog_pages_menu_body_gift(web_browser):
    # проверяет работу пункта меню "В подарок" в теле сайти
    page = CatalogPage(web_browser)  # открываем главную страницу
    page.menu_gift.click()  # Находим пункт меню "В подарок" и кликаем по нему

    assert page.menu_answer.get_text() == "В подарок"


@pytest.mark.regression
def test_catalog_pages_menu_remington(web_browser):
    # проверяет работу пункта меню "Remington" в теле сайти
    page = CatalogPage(web_browser)  # открываем главную страницу
    page.menu_remington.click()  # Находим пункт меню "Remington" и кликаем по нему

    assert page.menu_answer.get_text() == "Remington"


@pytest.mark.regression
def test_catalog_pages_menu_aqua(web_browser):
    # проверяет работу пункта меню "Аксессуары для оружия" в теле сайти
    page = CatalogPage(web_browser)  # открываем главную страницу
    page.menu_weapon.click()  # Находим пункт меню "Аксессуары для оружия" и кликаем по нему

    assert page.menu_answer.get_text() == "Аксессуары для оружия"


@pytest.mark.regression
def test_catalog_pages_menu_parts(web_browser):
    # проверяет работу пункта меню "Запасные части для оружия" в теле сайти
    page = CatalogPage(web_browser)  # открываем главную страницу
    page.menu_parts.click()  # Находим пункт меню "Запасные части для оружия" и кликаем по нему

    assert page.menu_answer.get_text() == "Запасные части для оружия"


@pytest.mark.regression
def test_catalog_pages_menu_permission(web_browser):
    # проверяет работу пункта меню "Как получить разрешение" в теле сайти
    page = CatalogPage(web_browser)  # открываем главную страницу
    page.menu_permission.click()  # Находим пункт меню "Как получить разрешение" и кликаем по нему

    assert page.menu_answer.get_text() == "Как получить разрешение"


@pytest.mark.regression
def test_catalog_pages_menu_boats(web_browser):
    # проверяет работу пункта меню "Лодки" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_boats.click()

    assert page.menu_answer.get_text() == "Лодки"


@pytest.mark.regression
def test_catalog_pages_menu_crossbows(web_browser):
    # проверяет работу пункта меню "Луки, Арбалеты" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_crossbows.click()

    assert page.menu_answer.get_text() == "Луки, Арбалеты"


@pytest.mark.regression
def test_catalog_pages_menu_knives(web_browser):
    # проверяет работу пункта меню "Ножи" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_knives.click()

    assert page.menu_answer.get_text() == "Ножи"


@pytest.mark.regression
def test_catalog_pages_menu_optics(web_browser):
    # проверяет работу пункта меню "Оптика" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_optics.click()

    assert page.menu_answer.get_text() == "Оптика"


@pytest.mark.regression
def test_catalog_pages_menu_gans(web_browser):
    # проверяет работу пункта меню "Оружие" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_gans.click()

    assert page.menu_answer.get_text() == "Оружие"


@pytest.mark.regression
def test_catalog_pages_menu_cartridges(web_browser):
    # проверяет работу пункта меню "Патроны" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_cartridges.click()

    assert page.menu_answer.get_text() == "Патроны"


@pytest.mark.regression
def test_catalog_pages_menu_protection(web_browser):
    # проверяет работу пункта меню "САМОЗАЩИТА" в теле сайти
    page = CatalogPage(web_browser)  # открываем главную страницу
    page.menu_protection.click()  # Находим пункт меню "Лодки" и кликаем по нему

    assert page.menu_answer.get_text() == "САМОЗАЩИТА"


@pytest.mark.regression
def test_catalog_pages_menu_safes(web_browser):
    # проверяет работу пункта меню "Сейфы оружейные" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_safes.click()

    assert page.menu_answer.get_text() == "Сейфы оружейные"


@pytest.mark.regression
def test_catalog_pages_menu_hunting(web_browser):
    # проверяет работу пункта меню "Товары для охоты и спорта" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_hunting.click()

    assert page.menu_answer.get_text() == "Товары для охоты и спорта"


@pytest.mark.regression
def test_catalog_pages_menu_tourism(web_browser):
    # проверяет работу пункта меню "Туризм" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_tourism.click()

    assert page.menu_answer.get_text() == "Туризм"


@pytest.mark.regression
def test_catalog_pages_menu_lanterns(web_browser):
    # проверяет работу пункта меню "Фонари" в теле сайти
    page = CatalogPage(web_browser)
    page.menu_lanterns.click()

    assert page.menu_answer.get_text() == "Фонари"
