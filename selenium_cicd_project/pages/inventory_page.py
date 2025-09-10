from selenium_cicd_project.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    PAEG_TITLE = (By.CLASS_NAME,'title')

    def __init__(self,driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_element_text(self.PAEG_TITLE)    