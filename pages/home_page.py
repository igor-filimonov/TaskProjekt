from pages.base import WebPage
from pages.elements import WebElement


class HomePage(WebPage):

    def __init__(self, web_driver):
        url = 'https://arsenal-ekb.com'
        super().__init__(web_driver, url)

    # Ссылки на социальные сети
    write_whatsapp = WebElement(xpath="//a[@title='Написать в WhatsApp']")
    write_telegram = WebElement(xpath="//a[@title='Написать в Telegram']")

    # Поиск
    magnifying_glass = WebElement(xpath="//a[@class='btn']//span[@class='icon']")
    search_input = WebElement(css_selector="input[placeholder='Поиск']")
    search_button = WebElement(css_selector='button[title="Искать"] span[class="icon"]')
    search_results = WebElement(css_selector='.string')

    # Контакты
    menu_item_contacts = WebElement(css_selector="div[class='h-right'] div[class='menu'] a")

    # Вход
    menu_item_input = WebElement(xpath="//span[contains(text(),'Вход')]")
    menu_item_input_username = WebElement(xpath="//input[@id='LoginForm_username']")
    menu_item_input_password = WebElement(xpath="//input[@id='LoginForm_password']")
    menu_item_input_button = WebElement(css_selector='input[value="Ok"]')
    menu_item_input_registration = WebElement(xpath="//p[@class='restore-btn']//a[contains(text(),'Регистрация')]")
    menu_item_input_forgot_password = WebElement(xpath="//a[contains(text(),'Я забыл пароль')]")
    menu_item_input_sms_error = WebElement(css_selector=".cms-error")
    menu_item_input_forgot_password_result = WebElement(css_selector="div[class='page-caption'] h1")
    menu_item_input_registration_result = WebElement(css_selector="div[class='page-caption'] h1")

    # Меню в шапке сайта
    menu_item_catalog = WebElement(xpath="//div[@class='h-menu']//span[contains(text(), 'Каталог')]")
    menu_item_news = WebElement(xpath="//div[@class='h-menu']//span[contains(text(),'Новости')]")
    menu_item_about = WebElement(xpath="//div[@class='h-menu']//span[contains(text(),'О магазине')]")
    menu_item_payment = WebElement(xpath="//div[@class='h-menu']//span[contains(text(),'Оплата, доставка и возврат')]")
    menu_item_info = WebElement(xpath="//div[@class='h-menu']//span[contains(text(),'Полезная информация')]")
    basket_number = WebElement(xpath="//span[@class='amount']")
    menu_results = WebElement(xpath="//body[1]/div[4]/div[2]/div[1]/ul[1]/li[3]/a[1]")
    basket_results = WebElement(xpath="//h1[contains(text(),'Корзина пуста')]")

    # Меню в теле сайта
    menu_body_weapon = WebElement(xpath="//a[contains(text(),'Оружие')]")
    menu_body_cartridges = WebElement(xpath="//a[contains(text(),'Патроны')]")
    menu_body_optical = WebElement(xpath="//a[contains(text(),'Оптические прицелы')]")
    menu_body_crossbows = WebElement(xpath="//a[contains(text(),'Луки, арбалеты')]")
    menu_body_safes = WebElement(xpath="//a[contains(text(),'Шкафы и оружейные сейфы')]")
    menu_body_gift = WebElement(xpath="//a[contains(text(),'варианты для подарков')]")
    menu_body_clothes = WebElement(xpath="//a[contains(text(),'Охотничья одежда и обувь')]")
    menu_body_results = WebElement(css_selector="div[class='page-caption'] h1")

    # Меню в подвале сайта
    menu_footer_catalog = WebElement(xpath="//div[@class='f-content']//span[contains(text(),'Каталог')]")
    menu_footer_news = WebElement(xpath="//div[@class='f-content']//span[contains(text(),'Новости')]")
    menu_footer_about = WebElement(xpath="//div[@class='f-content']//span[contains(text(),'О магазине')]")
    menu_footer_payment = WebElement(xpath="//div[@class='f-content']//span[contains(text(),"
                                           "'Оплата, доставка и возврат')]")
    menu_footer_info = WebElement(xpath="//div[@class='f-content']//span[contains(text(),'Полезная информация')]")
    menu_footer_development = WebElement(xpath="//a[@href='http://apri-code.ru']")
