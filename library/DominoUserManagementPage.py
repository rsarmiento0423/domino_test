""" DominoUserManagementPage.py """
import inspect
import random

from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoUserManagementPage(BaseFactory):
    """class: DominoUserManagementPage"""

    path = "/#/usermanagement"

    user_profile = (By.CSS_SELECTOR, '[data-test-id="user-profile"]')
    user_management_page_title = (By.XPATH, "//h2[normalize-space()='User management']")
    first_name_textbox = (
        By.CSS_SELECTOR,
        ' [data-test-id="UserAddControls"] [data-test-id="AddUserFirstNameInput"]',
    )
    last_name_textbox = (
        By.CSS_SELECTOR,
        '[data-test-id="UserAddControls"] [data-test-id="AddUserLastNameInput"]',
    )
    user_email_textbox = (
        By.CSS_SELECTOR,
        '[data-test-id="UserAddControls"]  [data-test-id="AddUserEmailInput"]',
    )
    accesstype_dropdown = (
        By.CSS_SELECTOR,
        '[data-test-id="UserAddControls"]  [data-test-id="AddUserAccessTypeSelect"]',
    )
    accesstype_admin = (By.XPATH, "//li[normalize-space()='Administrator']")
    accesstype_user = (By.XPATH, "//li[normalize-space()='User']")
    add_user_button = (
        By.CSS_SELECTOR,
        'div[data-test-id="UserAddControls"]  button[data-test-id="UserAddButton"]',
    )
    all_users_list_table = (
        By.CSS_SELECTOR,
        '[data-test-id="UserManagement-View"]  .MuiTable-root',
    )
    all_users_list_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="UserManagement-View"]  .MuiTableHead-root',
    )
    add_user_status_message = (
        By.CSS_SELECTOR,
        '[data-test-id="styled-snackbar-content"]',
    )
    user_management_email = (
        By.CSS_SELECTOR,
        "table > tbody > tr > td:nth-child(2) > p",
    )
    fail_to_add_user_message = (By.CSS_SELECTOR, '[data-test-id="snackbar-title"]')
    edit_user_button = (
        By.CSS_SELECTOR,
        "table > tbody > tr > td:nth-child(4) > div > div > button",
    )
    edit_first_name = (By.CSS_SELECTOR, '[data-test-id="EditUserFirstNameInput"]')
    edit_last_name = (By.CSS_SELECTOR, '[data-test-id="EditUserLastNameInput"]')
    edit_email = (By.CSS_SELECTOR, '[data-test-id="EditUserEmailInput"]')
    edit_role = (By.CSS_SELECTOR, "#edit-user-permission-select")
    edit_status = (By.CSS_SELECTOR, "#edit-user-status-select")
    edit_save_btn = (By.CSS_SELECTOR, '[data-test-id="SaveEditing"]')
    edit_cancel_btn = (By.CSS_SELECTOR, 'data-test-id="CancelEditing"')

    def go_to_user_management_page(self, url):
        """Method: go_to_user_management_page"""
        try:
            test = inspect.stack()[0][3]
            self.open(f"{url}{self.path}")
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def user_management_not_displayed_for_normal_users(self):
        """Method: user_management_not_displayed_for_normal_users"""
        try:
            test = inspect.stack()[0][3]
            time.sleep(3)
            assert (
                self.is_element_displayed(self.user_management_page_title, 30) is False
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise AssertionError(f"Failed {test} due to: {error}!")

    @staticmethod
    def generate_email(usertype):
        """Method: generate_email"""
        value = random.randint(100, 4000000000) + random.randint(100, 40000000)
        if usertype == "admin":
            email = "admin+" + str(value) + "@oneconcern.com"
        if usertype == "contributor":
            email = "contrib+" + str(value) + "@oneconcern.com"
        return email

    def add_new_normal_user_details(self):
        """Method: add_new_normal_user_details"""
        try:
            test = inspect.stack()[0][3]
            email = self.generate_email("contributor")
            self.wait_for_element_present(self.first_name_textbox, 100)
            self.send_keys_to_element(self.first_name_textbox, "Contributor")
            self.send_keys_to_element(self.last_name_textbox, "User")
            self.send_keys_to_element(self.user_email_textbox, email)
            print(f"New User Email: {email}")
            self.click_element(self.accesstype_dropdown)
            self.click_element(self.accesstype_user)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def add_new_admin_user_details(self):
        """Method: add_new_admin_user_details"""
        try:
            test = inspect.stack()[0][3]
            email = self.generate_email("admin")
            self.wait_for_element_present(self.first_name_textbox, 100)
            self.send_keys_to_element(self.first_name_textbox, "Admin")
            self.send_keys_to_element(self.last_name_textbox, "User")
            self.send_keys_to_element(self.user_email_textbox, email)
            print(f"New Admin User Email: {email}")
            self.click_element(self.accesstype_dropdown)
            self.click_element(self.accesstype_admin)
            print(f"PASS: {test}")
            return email
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def add_an_existing_user_details(self, email):
        """ " Method: add_an_existing_user_details"""
        try:
            ##try to add same user email again to make sure system validate and error message is displayed
            test = inspect.stack()[0][3]
            self.send_keys_to_element(self.first_name_textbox, "Existing")
            self.send_keys_to_element(self.last_name_textbox, "User")
            self.send_keys_to_element(self.user_email_textbox, email)
            print(f"Add Existing User Email: {email}")
            self.click_element(self.accesstype_dropdown)
            self.click_element(self.accesstype_user)
            self.wait_for_element_clickable(self.add_user_button, 100)
            self.click_element(self.add_user_button)
            self.wait_for_element_visible(self.add_user_status_message, 100)
            self.wait_for_element_present(self.add_user_status_message, 100)
            assert self.is_element_displayed(self.add_user_status_message, 100)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_add_user_button(self):
        """Method: click_add_user_button"""
        try:
            test = inspect.stack()[0][3]
            self.send_key_element(self.add_user_button)
            self.pause()
            assert self.is_element_enabled(self.add_user_button) is False
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def check_that_system_permit_external_domain(self, externaluser):
        """Method: check_that_system_permit_external_domain"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.first_name_textbox, 100)
            self.send_keys_to_element(self.first_name_textbox, "External")
            self.send_keys_to_element(self.last_name_textbox, "User")
            self.send_keys_to_element(self.user_email_textbox, externaluser)
            print(f"Add External User email: {externaluser}")
            self.click_element(self.accesstype_dropdown)
            self.click_element(self.accesstype_user)
            self.wait_for_element_clickable(self.add_user_button, 100)
            self.click_element(self.add_user_button)
            self.wait_for_element_visible(self.add_user_status_message, 100)
            self.wait_for_element_present(self.add_user_status_message, 100)
            assert self.is_element_displayed(self.add_user_status_message, 100)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_hidden_admin_user(self, admin_email):
        """Method: assert_hidden_admin_user"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.first_name_textbox, 100)
            email_elements = self.get_number_of_elements(self.user_management_email)
            total_email_elements = len(email_elements)
            print(f"Got total element: {total_email_elements}")
            for email in email_elements:
                print(f"Email: {email.text}")
                assert email.text != admin_email, f"Found email: {admin_email}"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def add_invalid_email(self):
        """Method: add_invalid_email"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.first_name_textbox, 100)
            self.send_keys_to_element(self.first_name_textbox, "Invalid")
            self.send_keys_to_element(self.last_name_textbox, "Email")
            self.send_keys_to_element(self.user_email_textbox, "123@junk.com")
            self.click_element(self.accesstype_dropdown)
            self.click_element(self.accesstype_user)
            self.wait_for_element_clickable(self.add_user_button, 100)
            self.click_element(self.add_user_button)
            self.wait_for_element_visible(self.fail_to_add_user_message, 100)
            self.wait_for_element_present(self.fail_to_add_user_message, 100)
            assert self.is_element_displayed(self.fail_to_add_user_message, 100)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def edit_existing_user_details(self):
        """Method: edit_existing_user_details"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.first_name_textbox, 100)
            self.click_element(self.edit_user_button)
            self.clear_element_text(self.edit_first_name)
            self.send_keys_to_element(self.edit_first_name, "First")
            first_name = self.get_attribute_value(self.edit_first_name)
            assert first_name == "First", "Mismatch First Name!"
            self.clear_element_text(self.edit_last_name)
            self.send_keys_to_element(self.edit_last_name, "Last")
            last_name = self.get_attribute_value(self.edit_last_name)
            assert last_name == "Last", "Mismatch Last Name!"
            self.click_element(self.edit_save_btn)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def add_first_last_name_empty_spaces(self):
        """ " Method: add_first_last_name_empty_spaces"""
        try:
            test = inspect.stack()[0][3]
            self.send_keys_to_element(self.first_name_textbox, "  ")
            self.send_keys_to_element(self.last_name_textbox, "  ")
            self.send_keys_to_element(
                self.user_email_textbox, "rsarmiento+usviewer1@oneconcern.com"
            )
            self.click_element(self.accesstype_dropdown)
            self.click_element(self.accesstype_user)
            assert self.is_element_enabled(self.add_user_button) is False
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
