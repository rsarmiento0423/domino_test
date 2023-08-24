""" DominoViewerUser.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoViewerUser(BaseFactory):
    """class: DominoViewerUser"""

    path = "/#/"
    manage_locations_button = (By.CSS_SELECTOR, '[data-test-id="manage-locations"]')
    locations_picker = (By.CSS_SELECTOR, '[data-test-id="locations-picker-button"]')
    at_risk_location_list = (By.CSS_SELECTOR, '[data-test-id="vulnerable-locations-list"]')

    def assert_at_risk_location_list_is_not_displayed(self):
        """Method: assert_at_risk_location_list_is_not_displayed"""
        assert self.is_element_displayed(self.at_risk_location_list, 30) is False

    def assert_manage_locations_button_is_not_displayed(self):
        """Method: assert_manage_locations_button_is_not_displayed"""
        test = inspect.stack()[0][3]
        try:
            assert (
                    self.is_element_displayed(self.manage_locations_button, 30) is False
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_locations_filter_dropdown_is_not_displayed(self):
        """Method: assert_locations_filter_dropdown_is_not_displayed"""

        test = inspect.stack()[0][3]
        try:
            assert (
                    self.is_element_displayed(self.locations_picker, 30) is False
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(inspect.stack()[0][3] + "_error")
            raise AssertionError(f"Failed {test} due to: {error}!")
