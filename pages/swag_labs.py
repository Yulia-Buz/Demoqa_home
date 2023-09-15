from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class Labs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def username(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def password(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True
