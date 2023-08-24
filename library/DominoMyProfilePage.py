""" DominoMyProfilePage.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoMyProfilePage(BaseFactory):
    """class: DominoMyProfilePage"""

    PAGE_URL = "/#/"

    user_profile = (By.CSS_SELECTOR, '[data-test-id="user-profile"]')
    my_profile_title = (By.CSS_SELECTOR, "#SettingsPanel > h2")
    username_value = (
        By.CSS_SELECTOR,
        '[data-test-id="MyProfileView"] .MuiTypography-body2:nth-child(1)',
    )
    edit_name_button = (By.CSS_SELECTOR, '[data-test-id="EditName"]')
    email_value = (
        By.CSS_SELECTOR,
        '[data-test-id="MyProfileView"] .MuiTypography-body2:nth-child(2)',
    )
    password_value = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-Display"] .MuiTypography-body2:nth-child(2)',
    )
    edit_password_button = (By.CSS_SELECTOR, '[data-test-id="PasswordForm-EditButton"]')
    edit_user_first_name_input = (
        By.CSS_SELECTOR,
        '[data-test-id="EditUserFirstNameInput"]',
    )
    edit_user_last_name_input = (
        By.CSS_SELECTOR,
        '[data-test-id="EditUserLastNameInput"]',
    )
    edit_user_cancel_button = (
        By.CSS_SELECTOR,
        '[data-test-id="MyProfileView"] .MuiButton-root:nth-child(1)',
    )
    edit_user_save_button = (
        By.CSS_SELECTOR,
        '[data-test-id="MyProfileView"] .MuiButton-root:nth-child(2)',
    )
    edit_password_current_password_input = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-CurrentPassword"]',
    )
    edit_password_new_password_input = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-NewPassword"]',
    )
    edit_password_confirm_password_input = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-ConfirmedPassword"]',
    )
    password_indicator_bar = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-StrengthIndicator"]',
    )
    edit_password_cancel_button = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-CancelButton"]',
    )
    edit_password_save_button = (
        By.CSS_SELECTOR,
        '[data-test-id="PasswordForm-SaveButton"]',
    )
    edit_password_status_message = (
        By.CSS_SELECTOR,
        '[data-test-id="styled-snackbar-content"]',
    )
    sign_out_button = (By.CSS_SELECTOR, '[data-test-id="Signout"]')
    map_bound_button = (By.CSS_SELECTOR, '[data-test-id="MapBoundsButton"]')

    def open_my_profile_page(self):
        """Method: open_my_profile_page"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.map_bound_button, 60)
            self.wait_for_element_present(self.user_profile, 60)
            self.wait_for_element_visible(self.user_profile, 60)
            self.click_element(self.user_profile)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def all_elements_on_user_profile_page_should_be_displayed(self, email):
        """Method: all_elements_on_user_profile_page_should_be_displayed"""
        try:
            test = inspect.stack()[0][3]
            time.sleep(1)
            self.wait_for_element_present(self.username_value, 30)
            self.wait_for_element_present(self.edit_name_button, 30)
            self.wait_for_element_present(self.email_value, 30)
            self.wait_for_element_present(self.edit_password_button, 30)
            user_email = self.get_text_from_element(self.email_value, 30)
            assert user_email == email
            password = self.get_text_from_element(self.password_value, 30)
            assert password == "••••••••"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def all_edit_user_name_fields_are_displayed(self):
        """Method: all_edit_user_name_fields_are_displayed"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.edit_name_button, 40)
            self.click_element(self.edit_name_button, 30)
            self.wait_for_element_present(self.edit_user_first_name_input, 30)
            self.wait_for_element_present(self.edit_user_last_name_input, 30)
            assert self.is_element_displayed(self.edit_user_first_name_input) is True
            assert self.is_element_displayed(self.edit_user_last_name_input) is True
            assert self.is_element_displayed(self.edit_user_cancel_button) is True
            assert self.is_element_displayed(self.edit_user_save_button) is True
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def cancel_edit_user_name(self, firstname, lastname):
        """Method: cancel_edit_user_name"""
        try:
            test = inspect.stack()[0][3]
            time.sleep(1)
            current_user_firstname_value = self.get_attribute_value(
                self.edit_user_first_name_input, 30
            )
            current_user_lastname_value = self.get_attribute_value(
                self.edit_user_last_name_input, 30
            )
            assert current_user_firstname_value == firstname
            assert current_user_lastname_value == lastname
            self.click_element(self.edit_user_cancel_button, 30)
            self.wait_for_element_present(self.username_value, 30)
            username = self.get_text_from_element(self.username_value, 30)
            time.sleep(1)
            assert (
                username == current_user_firstname_value + " " + current_user_lastname_value
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_edit_user_name_button(self):
        """Method: click_edit_user_name_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.edit_name_button, 40)
            self.click_element(self.edit_name_button, 30)
            self.wait_for_element_present(self.edit_user_first_name_input, 30)
            self.wait_for_element_present(self.edit_user_save_button, 30)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def edit_user_name(self, newfirstname, newlastname):
        """Method: edit_user_name"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.user_profile, 30)
            self.click_element(self.user_profile, 30)
            self.wait_for_element_present(self.edit_name_button, 40)
            self.click_element(self.edit_name_button, 30)
            self.wait_for_element_present(self.edit_user_first_name_input, 30)
            self.wait_for_element_present(self.edit_user_save_button, 30)
            self.clear_element_text(self.edit_user_first_name_input, 60)
            self.send_keys_to_element(self.edit_user_first_name_input, newfirstname, 30)
            self.clear_element_text(self.edit_user_last_name_input, 60)
            self.send_keys_to_element(self.edit_user_last_name_input, newlastname, 30)
            self.click_element(self.edit_user_save_button, 30)
            self.wait_for_element_present(self.username_value, 30)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_user_name_value(
        self, newfirstname, newlastname, oldfirstname, oldlastname
    ):
        """Method: edit_user_name"""
        try:
            test = inspect.stack()[0][3]
            username = self.get_text_from_element(self.username_value, 30)
            assert username == newfirstname + " " + newlastname
            # need to change the username to the old value to avoid failure for Cancel edit username test
            self.click_element(self.edit_name_button, 30)
            self.wait_for_element_present(self.edit_user_first_name_input, 40)
            self.wait_for_element_present(self.edit_user_last_name_input, 40)
            self.clear_element_text(self.edit_user_first_name_input, 60)
            self.clear_element_text(self.edit_user_last_name_input, 60)
            self.send_keys_to_element(self.edit_user_first_name_input, oldfirstname, 30)
            self.send_keys_to_element(self.edit_user_last_name_input, oldlastname, 30)
            self.click_element(self.edit_user_save_button, 30)
            self.wait_for_element_present(self.username_value, 30)
            username = self.get_text_from_element(self.username_value, 30)
            assert username == oldfirstname + " " + oldlastname
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def all_edit_user_password_fields_are_displayed(self):
        """Method: all_edit_user_password_fields_are_displayed"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.edit_password_button, 40)
            self.click_element(self.edit_password_button, 30)
            self.wait_for_element_present(self.edit_password_current_password_input, 30)
            self.wait_for_element_present(self.edit_password_new_password_input, 30)
            assert (
                self.is_element_displayed(self.edit_password_current_password_input, 30)
                is True
            )
            assert (
                self.get_attribute_value(self.edit_password_current_password_input, 30)
                == ""
            )
            assert (
                self.is_element_displayed(self.edit_password_new_password_input, 30) is True
            )
            assert (
                self.is_element_displayed(self.edit_password_confirm_password_input, 30)
                is True
            )
            assert self.get_attribute_value(self.edit_password_new_password_input, 30) == ""
            assert (
                self.get_attribute_value(self.edit_password_confirm_password_input, 30)
                == ""
            )
            assert self.is_element_displayed(self.password_indicator_bar, 30) is True
            assert self.is_element_displayed(self.edit_password_cancel_button, 30) is True
            assert self.is_element_displayed(self.edit_password_save_button, 30) is True
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def cancel_edit_password(self):
        """Method: cancel_edit_password"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.edit_password_current_password_input, 30)
            self.click_element(self.edit_password_cancel_button, 30)
            assert self.is_element_displayed(self.edit_password_button, 30) is True
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def edit_user_password(self, oldpassword, newpassword):
        """Method: edit_user_password"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.edit_password_button, 40)
            self.send_keys_to_element(
                self.edit_password_current_password_input, oldpassword, 30
            )
            self.send_keys_to_element(
                self.edit_password_new_password_input, newpassword, 30
            )
            self.send_keys_to_element(
                self.edit_password_confirm_password_input, newpassword, 30
            )
            time.sleep(5)
            self.click_element(self.edit_password_save_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def edit_password_success_message_should_be_visible(self):
        """Method: edit_password_success_message_should_be_visible"""
        try:
            test = inspect.stack()[0][3]
            time.sleep(5)
            self.wait_for_element_present(self.edit_password_status_message, 100)
            success_msg = self.get_text_from_element(self.edit_password_status_message, 100)
            assert success_msg == "Success! Your password was changed."
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def log_out_from_profile_page(self):
        """Method: log_out_from_profile_page"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.sign_out_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def edit_password_error_message_should_be_visible(self):
        """Method: edit_password_error_message_should_be_visible"""
        try:
            test = inspect.stack()[0][3]
            time.sleep(5)
            self.wait_for_element_present(self.edit_password_status_message, 120)
            error_msg = self.get_text_from_element(self.edit_password_status_message, 120)
            assert error_msg == "The password you entered was incorrect."
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_edit_password_button(self):
        """Method: click_edit_password_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.edit_password_button, 40)
            self.click_element(self.edit_password_button, 30)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def check_edit_password_save_button_is_disabled_untill_all_fields_are_valid(
        self, invalidpassword
    ):
        """Method: check_edit_password_save_button_is_disabled_untill_all_fields_are_valid"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.edit_password_current_password_input, 30)
            # Make sure Save button is disabled
            assert self.is_element_enabled(self.edit_password_save_button, 30) is False
            # Enter invalid passwords, less than 10 digits
            self.send_keys_to_element(
                self.edit_password_current_password_input, invalidpassword, 30
            )
            self.send_keys_to_element(
                self.edit_password_new_password_input, invalidpassword, 30
            )
            self.send_keys_to_element(
                self.edit_password_confirm_password_input, invalidpassword, 30
            )
            time.sleep(3)
            assert self.is_element_enabled(self.edit_password_save_button, 30) is False
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
