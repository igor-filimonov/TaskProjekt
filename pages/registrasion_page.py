from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class RegistrasionPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://arsenal-ekb.com/registration'
        super().__init__(web_driver, url)

    email = WebElement(xpath="//input[@id='FormModel_mail']")
    password1 = WebElement(xpath="//input[@id='FormModel_password']")
    password2 = WebElement(xpath="//input[@id='FormModel_confirm']")
    name1 = WebElement(xpath="//input[@id='FormModel_f_name']")
    name2 = WebElement(xpath="//input[@id='FormModel_i_name']")
    phone = WebElement(xpath="//input[@id='FormModel_phone']")
    box = WebElement(css_selector="label[for='FormModel_agree'] span[class='icon']")
    button = WebElement(xpath="//input[@name='send']")

    answer2 = ManyWebElements(css_selector=".errorSummary ul li")
    answer1 = WebElement(xpath="(//span[@class='string'])[1]")

    sms_error1 = WebElement(css_selector=".cms-error")
    sms_error2 = ManyWebElements(xpath="//div[@class='errorSummary']//ul")
    sms_error_phone = WebElement(css_selector="div[class='notifications phone-mask-errors'] li[class='cms-error']")
    sms_error_password = WebElement(xpath="//li[contains(text(),'Пароль и подтверждение должны совпадать')]")
    sms_error_box = WebElement(xpath="//li[contains(text(),'Необходимо дать согласие на обработку данных')]")
