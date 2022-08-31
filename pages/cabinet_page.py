from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class CabinetPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://arsenal-ekb.com/'
        super().__init__(web_driver, url)

    # Вход в аккаунт
    menu_item_input = WebElement(xpath="//span[contains(text(),'Вход')]")
    menu_item_input_username = WebElement(xpath="//input[@id='LoginForm_username']")
    menu_item_input_password = WebElement(xpath="//input[@id='LoginForm_password']")
    menu_item_input_button = WebElement(css_selector='input[value="Ok"]')

    # кнопки в хапке сайта для входа в кабинет и сообщения
    cabinet = WebElement(css_selector="body > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) >"
                                      " div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > "
                                      "p:nth-child(1) > a:nth-child(2)")    # Кнопка входа в кабинет с именем
    messages = WebElement(css_selector="a[title='Сообщения'] span[class='icon']")  # Кнопка сообщение

    # пункты меню в личном кабинете
    cabinet_answer = WebElement(css_selector=".header")  # надпись "Личный кабинет"
    header_answer = WebElement(css_selector="div[class='page-caption'] h1")  # заголовок страницы

    menu_orders = WebElement(xpath="//span[contains(text(),'Мои заказы')]")  # Пункт меню "Мои заказы"
    menu_messages = WebElement(xpath="//span[contains(text(),'Сообщения')]")  # Пункт меню "Сообщения"
    menu_personal_data = WebElement(xpath="//span[contains(text(),'Личные данные')]")  # Пункт меню "Личные данные"

    # отправка сообщения менеджеру
    input_messages = WebElement(xpath="//textarea[@placeholder='Введите текст сообщения']")  # поле ввода сообщения
    button_messages = WebElement(xpath="//input[@name='send']")                 # кнопка отправить сообщение

    # вкладка "Личные данные"
    menu_edit = WebElement(xpath="(//a[contains(text(),'редактировать')])[1]")
    menu_add_address = WebElement(xpath="//span[contains(text(),'Добавить адрес')]")
    menu_change_password = WebElement(xpath="//a[contains(text(),'сменить пароль')]")

    # изменение личных данных
    edit_answer = WebElement(css_selector="div[class='header'] p")
    edit_email = WebElement(xpath="(//input[@name='Users[login]'])[1]")
    edit_i_name = WebElement(xpath="(//input[@name='UserData[i_name]'])[1]")
    edit_f_name = WebElement(xpath="(//input[@name='UserData[f_name]'])[1]")
    edit_o_name = WebElement(xpath="(//input[@name='UserData[o_name]'])[1]")
    edit_phone = WebElement(xpath="//input[@placeholder='+7(___) ___-__-__']")
    edit_button = WebElement(css_selector="input[value='Сохранить']")
    sms = WebElement(xpath="//li[@class='cms-message']")

    # добавление адреса
    add_answer = WebElement(css_selector="div[class='header'] p")
    add_city = WebElement(css_selector="input[name='UserAddresses[city]']")
    add_index = WebElement(css_selector="input[name='UserAddresses[index]']")
    add_street = WebElement(css_selector="input[name='UserAddresses[street]']")
    add_house = WebElement(css_selector="input[name='UserAddresses[house]']")
    add_room = WebElement(css_selector="input[name='UserAddresses[room]']")
    add_button = WebElement(css_selector="input[value='Сохранить']")

    edit_address = WebElement(xpath="(//a[@class='profile-action popup-dialog-btn']"
                                    "[contains(text(),'редактировать')])[2]")
    clear_address = WebElement(css_selector="input[value='Удалить адрес']")
