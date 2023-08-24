""" DominoEntitlementsPage.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoEntitlementsPage(BaseFactory):
    """class: DominoEntitlementsPage"""

    path = "/#/locations"
    hazards = (By.CSS_SELECTOR, '[data-test-id="HazardFilterButton"]')
    floods = (By.CSS_SELECTOR, '[data-test-id="HazardSelector-FLOOD"]')
    wind = (By.CSS_SELECTOR, '[data-test-id="HazardSelector-WIND"]')
    earthquake = (By.CSS_SELECTOR, '[data-test-id="HazardSelector-EARTHQUAKE"]')
    hazard_elements = (By.CSS_SELECTOR, 'div[data-test-id="HazardSelector-menu"] ul li')
    at_risk_locations_side_panel = (By.CSS_SELECTOR, '[data-test-id="SidePanel-Wrapper"]')
    at_risk_location = (By.CSS_SELECTOR, '[data-test-id="VulnerableLocationsList-content"] li')

    def click_hazards_dropdown(self):
        """Method: click_hazards_dropdown"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.at_risk_locations_side_panel, 30)
            self.wait_for_element_clickable(self.hazards, 30)
            self.click_element(self.hazards)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def select_earth_quake(self):
        """Method: select_earth_quake"""
        test = inspect.stack()[0][3]
        try:
            self.click_element(self.earthquake)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_hazards_dropdown_has_only_floods(self):
        """Method: assert_hazards_dropdown_has_only_floods"""
        test = inspect.stack()[0][3]
        try:
            number_of_hazards = self.get_number_of_elements(self.hazard_elements, 30)
            assert len(number_of_hazards) == 1
            assert self.is_element_present(self.floods) is True
            assert self.is_element_present(self.earthquake) is False
            assert self.is_element_present(self.wind) is False
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_hazards_dropdown_has_only_floods_and_earthquakes(self):
        """Method: assert_hazards_dropdown_has_only_floods_and_earthquakes"""
        test = inspect.stack()[0][3]
        try:
            number_of_hazards = self.get_number_of_elements(self.hazard_elements, 30)
            assert len(number_of_hazards) == 2
            assert self.is_element_present(self.floods) is True
            assert self.is_element_present(self.earthquake) is True
            assert self.is_element_present(self.wind) is False
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_a_location(self):
        """Method: assert_hazards_dropdown_has_only_floods_and_earthquakes"""
        test = inspect.stack()[0][3]
        try:
            self.click_element(self.at_risk_location, 20)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_hazards_dropdown_has_all_entitlements(self):
        """Method: assert_dropdown_has_all_entitlements"""
        test = inspect.stack()[0][3]
        try:
            number_of_hazards = self.get_number_of_elements(self.hazard_elements, 30)
            assert len(number_of_hazards) == 3
            assert self.is_element_present(self.floods) is True
            assert self.is_element_present(self.earthquake) is True
            assert self.is_element_present(self.wind) is True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
