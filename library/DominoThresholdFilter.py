""" DominoThresholdFilter.py """
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoThresholdFilter(BaseFactory):
    """class: DominoThresholdFilter"""

    planning_horizon_button = (By.CSS_SELECTOR, '[data-test-id="PLANNING_HORIZON-picker-button"]')
    threshold_button = (By.CSS_SELECTOR, '[data-test-id="thresholds-PickerForm"]')
    restore_button = (By.NAME, 'resetToDefaults')
    apply_button = (By.NAME, 'apply')
    threshold_setting_text = (By.CSS_SELECTOR, '[data-test-id="picker-button-subtext"]')
    building_percentage = (By.ID, 'structuralDamage')
    building_percentage = (By.ID, 'structuralDamage')
    power_input = (By.ID, 'powerDowntime-days')

    def edit_threshold_assumption(self, building_data, power_data):
        """Method: edit_threshold_assumption"""
        try:
            self.wait_for_element_clickable(self.threshold_button)
            if self.get_text_from_element(self.threshold_setting_text) == "Custom":
                self.click_element(self.threshold_button)
                self.click_element(self.restore_button)
                self.click_element(self.apply_button)
            time.sleep(1)
            assert self.get_text_from_element(self.threshold_setting_text) == "Default"
            self.click_element(self.threshold_button)
            self.send_keys_to_element(self.building_percentage, building_data)
            self.send_keys_to_element(self.power_input, power_data)
            self.click_element(self.apply_button)
            self.click_element(self.threshold_button)
        except Exception as error:
            raise Exception(f"Something went wrong {error}")

    def assert_threshold_assumptions_changed(self, building_data, power_data):
        """Method: assert_threshold_assumptions_changed"""
        try:
            assert self.get_attribute_value(self.building_percentage) == building_data
            assert self.get_attribute_value(self.power_input) == power_data
        except AssertionError as error:
            raise AssertionError(f"Assertion failed due to: {error}!")
