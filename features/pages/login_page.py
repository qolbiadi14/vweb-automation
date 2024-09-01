from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.driver.maximize_window()

    def navigate(self):
        self.driver.get(self.base_url)
        
    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, 'loginform-username')
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, 'loginform-password')
        password_field.send_keys(password)

    def solve_captcha(self):
        time.sleep(2)
        captcha_response = self.driver.find_element(By.ID, 'g-recaptcha-response')
        self.driver.execute_script("arguments[0].style.display = 'block';", captcha_response)
        captcha_response.send_keys('PASSED')
        captcha_response.send_keys(Keys.TAB)

    def click_login(self):
        login_button = self.driver.find_element(By.ID, 'btnlogin') 
        login_button.click()

    def close_modal_if_present(self):
        time.sleep(5)
        try:
            modal_dialog = self.driver.find_element(By.ID, 'gg')
            if modal_dialog.is_displayed():
                close_button = self.driver.find_element(By.ID, 'kembali1')
                close_button.click()
        except NoSuchElementException:
            pass

    def get_alert_warning(self):
        try:
            alert_warning = self.driver.find_element(By.CLASS_NAME, 'alert-warning')
            return alert_warning
        except NoSuchElementException:
            return None