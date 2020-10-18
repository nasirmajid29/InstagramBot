from time import sleep
from selenium import webdriver


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element_by_id('loginForm').click()
        sleep(2)
        return LoginPage(self.browser)


self = webdriver.Chrome()
self.implicitly_wait(5)

home_page = HomePage(self)
login_page = home_page.go_to_login_page()
login_page.login("wholesomebot42", "sd@2CYG8WKdPz7gNbMkxdGF*WUtbr3tldc1HRxr&K074w0Q&£p")
self.close()
