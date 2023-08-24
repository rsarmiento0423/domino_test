""" DominoClimateToggle.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoClimateToggle(BaseFactory):
    """class: DominoClimateToggle"""

    PAGE_URL = "/#/"

    climate_toggle_button = (By.CSS_SELECTOR, '[data-test-id="climate-toggle"]')
    climate_toggle_label = (By.CSS_SELECTOR, '[data-test-id="climate-toggle-label"]')

    def edit_climate_assumptions(self):
        """Method: edit_climate_assumptions"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_present(self.climate_toggle_label, 30)
            climate_label = self.get_text_from_element(self.climate_toggle_label)
            if climate_label == "On":
                self.wait_for_element_clickable(self.climate_toggle_button, 30)
                self.click_element(self.climate_toggle_button)
                assert self.get_text_from_element(self.climate_toggle_label) == "Off"
            else:
                self.wait_for_element_clickable(self.climate_toggle_button, 30)
                self.click_element(self.climate_toggle_button)
                assert self.get_text_from_element(self.climate_toggle_label) == "On"
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")
