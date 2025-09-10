from selenium_cicd_project.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage(BasePage):
    
    USERNAME = (By.ID,'user-name')
    PASSWORD_INPUT = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get('https://www.saucedemo.com')

    def enter_username(self,username):
        self.do_send_keys(self.USERNAME,username)    

    def enter_password(self,password):
        self.do_send_keys(self.PASSWORD_INPUT, password)
        

    def click_login_button(self):
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(15)

    def get_error_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text             
