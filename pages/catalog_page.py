from pages.base import WebPage
from pages.elements import WebElement


class CatalogPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://arsenal-ekb.com/catalogue/podarochnye-sertifikaty'
        super().__init__(web_driver, url)

    # меню каталога
    menu_gift = WebElement(xpath="//span[contains(text(),'В подарок')]")
    menu_remington = WebElement(xpath="//span[normalize-space()='Remington']")
    menu_aqua = WebElement(xpath="//span[contains(text(),'Аква МотоТехника')]")
    menu_weapon = WebElement(xpath="//span[contains(text(),'Аксессуары для оружия')]")
    menu_parts = WebElement(xpath="//span[contains(text(),'Запасные части для оружия')]")
    menu_permission = WebElement(xpath="//span[contains(text(),'Как получить разрешение')]")
    menu_boats = WebElement(xpath="//span[contains(text(),'Лодки')]")
    menu_crossbows = WebElement(xpath="//span[contains(text(),'Луки, Арбалеты')]")
    menu_knives = WebElement(xpath="//span[contains(text(),'Ножи')]")
    menu_optics = WebElement(xpath="//span[contains(text(),'Оптика')]")
    menu_gans = WebElement(xpath="//span[contains(text(),'Оружие')]")
    menu_cartridges = WebElement(xpath="//span[contains(text(),'Патроны')]")
    menu_protection = WebElement(xpath="//span[contains(text(),'САМОЗАЩИТА')]")
    menu_safes = WebElement(xpath="//span[contains(text(),'Сейфы оружейные')]")
    menu_hunting = WebElement(xpath="//span[contains(text(),'Товары для охоты и спорта')]")
    menu_tourism = WebElement(xpath="//span[contains(text(),'Туризм')]")
    menu_lanterns = WebElement(xpath="//span[contains(text(),'Фонари')]")
    menu_answer = WebElement(css_selector="div[class='page-caption'] h1")

