""" DominoLoginPage.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoLoginPage(BaseFactory):
    """class: DominoLoginPage"""

    PAGE_URL = "/#/"

    login_frame = (By.ID, "login-iframe")
    username_field = (By.CSS_SELECTOR, "#username")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#kc-login")
    remember_me_checkbox = (By.CSS_SELECTOR, "#rememberMe")
    user_profile = (By.CSS_SELECTOR, '[data-test-id="user-profile"]')
    invalid_credentials = (
        By.CSS_SELECTOR,
        'div[class="alert alert-error"] span[class="c-snackbar--error"]',
    )
    forget_password_link = (By.CSS_SELECTOR, "#kc-forgot-pword-link")
    reset_password_header = (By.CSS_SELECTOR, 'h2[class="kc-pages-title"]')
    manage_locations_button = (By.CSS_SELECTOR, '[data-test-id="secondary-nav"]')
    sign_out_button = (By.CSS_SELECTOR, '[data-test-id="Signout"]')

    def go_to_domino(self, url):
        """Method: go_to_domino"""
        try:
            test = inspect.stack()[0][3]
            self.open(url)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def log_in(self, username, password):
        """Method: log_in"""
        try:
            test = inspect.stack()[0][3]
            print("Logging into Domino as: {}".format(username))
            self.wait_for_element_present(self.login_frame, 30)
            WebDriverWait(self.browser, 10).until(
                EC.frame_to_be_available_and_switch_to_it(self.login_frame)
            )
            self.wait_for_element_present(self.username_field)
            self.clear_element_text2(self.username_field)
            self.send_keys_to_element(
                self.username_field, text=username, sensitive=True
            )
            self.send_keys_to_element(
                self.password_field, text=password, sensitive=True
            )
            self.click_element(self.remember_me_checkbox)
            self.click_element(self.login_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def log_out(self):
        """Method: log_out"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.user_profile, 120)
            self.click_element(self.user_profile)
            self.click_element(self.sign_out_button)
            print(f"PASS: {test}")
            return True
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def invalid_credentials_should_show(self):
        """Method: invalid_credentials_should_show"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.invalid_credentials)
            alert = self.get_text_from_element(self.invalid_credentials)
            assert alert == "Invalid credentials"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
