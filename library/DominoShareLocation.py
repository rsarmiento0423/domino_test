""" DominoShareLocation.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoShareLocation(BaseFactory):
    """class: DominoShareLocation"""

    path = "/#/analysis"
    at_risk_location_list = (
        By.CSS_SELECTOR,
        '[data-test-id="vll-location-counts-container"]',
    )
    at_risk_total_locations = (
        By.CSS_SELECTOR,
        '[data-test-id="TotalLocations-loc-count"]',
    )
    first_at_risk_location = (By.CSS_SELECTOR, "ul > li:nth-child(1)")
    share_location_button = (By.LINK_TEXT, "Share Location")
    share_location_dialog = (By.CSS_SELECTOR, '[data-test-id="ShareModal-Title"]')
    firstname_share_location = (
        By.CSS_SELECTOR,
        '[data-test-id="ShareModal-FirstName"]',
    )
    lastname_share_location = (By.CSS_SELECTOR, '[data-test-id="ShareModal-LastName"]')
    email_share_location = (By.CSS_SELECTOR, '[data-test-id="ShareModal-email"]')
    share_button = (By.CSS_SELECTOR, '[data-test-id="ShareLocationModal-ShareButton"]')
    cancel_button = (
        By.CSS_SELECTOR,
        '[data-test-id="ShareLocationModal-CancelShareButton"]',
    )
    snack_bar_message = (By.CSS_SELECTOR, '[data-test-id="snackbar-title"]')
    at_risk_location_name = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationDetailCard"] > div > div > h2',
    )

    def verify_at_risk_locations(self):
        """Method: verify_at_risk_locations"""
        try:
            test = inspect.stack()[0][3]
            page_url = self.browser.current_url
            print(f"Got page URL: {page_url}")
            assert self.wait_for_element_visible(
                self.at_risk_location_list, 120
            ), "Error displaying At-risk locations!"
            assert self.wait_for_element_visible(
                self.at_risk_total_locations, 120
            ), "Unable to find total locations!"
            i = 0
            while i < 2:
                self.pause(1)
                total_locations = self.get_text_from_element(
                    self.at_risk_total_locations
                )
                print(f"Got total locations for iteration {i}: {total_locations}")
                int_total = self.extract_num(total_locations)
                print(f"Got total: {int_total}!")
                if int_total > 0:
                    break
                self.browser.refresh()
                self.pause(3)
                i += 1
            assert int_total > 0, "Expected a number of At-risk locations!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_at_risk_location(self):
        """Method click_at_risk_location"""
        try:
            test = inspect.stack()[0][3]
            self.verify_at_risk_locations()
            assert self.wait_for_element_visible(
                self.first_at_risk_location, 120
            ), "Error displaying first At-risk location!"
            self.click_element(self.first_at_risk_location)
            self.pause(5)
            assert self.wait_for_element_visible(
                self.at_risk_location_name, 120
            ), "Error displaying first At-risk location name!"
            self.generate_screenshot(test + "_with_at_risk_location_name")
            location_name = self.get_text_from_element(self.at_risk_location_name)
            print(f"Location name: {location_name}")
            assert len(location_name) > 0, "Missing location name!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_share_location_button(self):
        """Method: click_share_location_button"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.share_location_button)
            assert self.wait_for_element_present(
                self.share_location_dialog
            ), "Unable to find Share location dialog!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def fill_out_share_location_dialog(self, fname, lname, email):
        """Method: fill_out_share_location_dialog"""
        try:
            test = inspect.stack()[0][3]
            assert self.wait_for_element_visible(
                self.share_location_dialog, 100
            ), "Unable to find Share location dialog!"
            self.send_keys_to_element(self.firstname_share_location, fname, 100)
            self.send_keys_to_element(self.lastname_share_location, lname, 100)
            self.send_keys_to_element(self.email_share_location, email, 100)
            self.click_element(self.share_button)
            self.pause(5)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def enter_bad_inputs_to_share_location(self, fname, lname, email):
        """Method: enter_bad_inputs_share_location"""
        try:
            test = inspect.stack()[0][3]
            self.fill_out_share_location_dialog(fname, lname, email)
            response = self.get_text_from_element(self.snack_bar_message)
            print(f"Got response: {response}")
            assert (
                response == "Failed to share the location"
            ), "Expected failure to send invite!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def enter_valid_inputs_to_share_location(self, fname, lname, email):
        """Method: enter_inputs_share_location"""
        try:
            test = inspect.stack()[0][3]
            self.fill_out_share_location_dialog(fname, lname, email)
            response = self.get_text_from_element(self.snack_bar_message)
            print(f"Got response: {response}")
            assert (
                response
                == f"An invitation to see this location has been sent to {email}"
            ), "Fail to send invite!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def cancel_inputs_to_share_location(self, fname, lname, email):
        """Method: cancel_inputs_share_location"""
        try:
            test = inspect.stack()[0][3]
            assert self.wait_for_element_visible(
                self.share_location_dialog, 100
            ), "Unable to find Share location dialog!"
            self.send_keys_to_element(self.firstname_share_location, fname, 100)
            self.send_keys_to_element(self.lastname_share_location, lname, 100)
            self.send_keys_to_element(self.email_share_location, email, 100)
            self.click_element(self.cancel_button)
            assert (
                self.is_element_displayed(self.share_location_dialog) is False
            ), "Share location dialog should not be displayed!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def verify_share_button_disabled(self, fname, lname, email):
        """Method: verify_share_button_disabled"""
        try:
            test = inspect.stack()[0][3]
            if fname == "spaces":
                fname = "  "
            if lname == "spaces":
                lname = "  "
            if email == "spaces":
                email = "  "
            assert self.wait_for_element_visible(
                self.share_location_dialog, 120
            ), "Unable to find Share location dialog!"
            if fname != "blank":
                self.send_keys_to_element(self.firstname_share_location, fname)
            if lname != "blank":
                self.send_keys_to_element(self.lastname_share_location, lname)
            if email != "blank":
                self.send_keys_to_element(self.email_share_location, email)
            self.pause(2)
            assert (
                self.is_element_enabled(self.share_button) is False
            ), "Share button should not be enabled!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def verify_share_button_not_visible(self):
        """Method: verify_share_button_not_visible"""
        try:
            test = inspect.stack()[0][3]
            assert (
                self.is_element_present(self.share_location_button) is False
            ), "Share location button should not be visible!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
