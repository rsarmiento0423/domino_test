""" DominoReturnPeriodFilter.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoReturnPeriodFilter(BaseFactory):
    """class: DominoReturnPeriodFilter"""

    PAGE_URL = "/#/"

    return_period_main_text = (
        By.XPATH,
        "//span[@data-test-id='picker-button-maintext'][contains(text(), 'Return period') or contains(text(), 'Planning horizon')]",
    )
    return_period_sub_text = (
        By.CSS_SELECTOR,
        'div[data-test-id="RETURN_PERIOD-PickerForm"] span[data-test-id="picker-button-subtext"]',
    )
    planning_horizon_sub_text = (
        By.CSS_SELECTOR,
        'div[data-test-id="PLANNING_HORIZON-PickerForm"] span[data-test-id="picker-button-subtext"]',
    )
    planning_horizon_radio_btn = (
        By.CSS_SELECTOR,
        '[data-test-id="PLANNING_HORIZON-PickerForm-form"] .MuiFormControlLabel-root:nth-child(1)',
    )
    return_period_radio_btn = (By.XPATH, "//p[normalize-space()='Return period']")
    slider_wrapper_period_text = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"]  .MuiTypography-root',
    )
    period_slider_marker = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"]   .MuiSlider-thumbColorPrimary',
    )
    period_first_marker = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"] [data-index="0"].MuiSlider-mark',
    )
    period_second_marker = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"] [data-index="1"].MuiSlider-mark',
    )
    period_third_marker = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"] [data-index="2"].MuiSlider-mark',
    )
    period_fourth_marker = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"] [data-index="3"].MuiSlider-mark',
    )
    period_fifth_marker = (
        By.CSS_SELECTOR,
        '[data-test-id="slider-outer-wrapper"] [data-index="4"].MuiSlider-mark',
    )
    restore_defaults_btn = (
        By.CSS_SELECTOR,
        '[data-test-id="PLANNING_HORIZON-PickerForm-form"]  .MuiButton-root:nth-child(1)',
    )
    apply_btn = (By.XPATH, "(//button[@name='apply'][normalize-space()='Apply'])[2]")
    custom_scale_control = (
        By.CSS_SELECTOR,
        '[data-test-id="CustomScaleControl-container"]',
    )

    def user_select_period_filter(self):
        """Method: user_select_period_filter"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_visible(self.return_period_main_text, 100)
            self.click_element(self.return_period_main_text, 30)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def user_chooses_planning_horizon_year(self, year, slidertext):
        """Method: user_chooses_planning_horizon_year"""
        try:
            # Select planning horizon filter and all periods on slider
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.custom_scale_control, 100)
            self.wait_for_element_visible(self.custom_scale_control, 100)
            self.wait_for_element_present(self.return_period_main_text, 100)
            self.click_element(self.return_period_main_text, 120)
            year_dict = {
                "1": self.period_first_marker,
                "5": self.period_second_marker,
                "10": self.period_third_marker,
                "20": self.period_fourth_marker,
                "30": self.period_fifth_marker,
            }
            self.wait_for_element_present(self.planning_horizon_radio_btn, 120)
            self.click_element(self.planning_horizon_radio_btn)
            self.click_element(year_dict.get(year))
            time.sleep(2)
            assert (
                    self.get_text_from_element(self.slider_wrapper_period_text)
                    == slidertext
            )
            self.click_element(self.apply_btn)
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def planning_horizon_filter_texts_should_be_changed(self, maintext, subtext):
        """Method: planning_horizon_filter_texts_should_be_changed"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.return_period_main_text, 100)
            self.wait_for_element_present(self.planning_horizon_sub_text, 100)
            assert self.get_text_from_element(self.return_period_main_text) == maintext
            assert self.get_text_from_element(self.planning_horizon_sub_text) == subtext
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def return_period_filter_texts_should_be_changed(self, maintext, subtext):
        """Method: return_period_filter_texts_should_be_changed"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.return_period_main_text, 100)
            self.wait_for_element_present(self.return_period_sub_text, 100)
            assert self.get_text_from_element(self.return_period_main_text) == maintext
            assert self.get_text_from_element(self.return_period_sub_text) == subtext
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def user_chooses_return_period_year(self, year, slidertext):
        """Method: user_chooses_return_period_year"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.return_period_main_text, 100)
            time.sleep(3)
            self.click_element(self.return_period_main_text, 30)
            year_dict = {
                "50": self.period_first_marker,
                "100": self.period_second_marker,
                "250": self.period_third_marker,
                "500": self.period_fourth_marker,
                "1000": self.period_fifth_marker,
            }
            self.wait_for_element_present(self.return_period_radio_btn, 60)
            time.sleep(1)
            self.click_element(self.return_period_radio_btn)
            time.sleep(1)
            self.click_element(year_dict.get(year))
            assert self.get_text_from_element(self.slider_wrapper_period_text) == slidertext
            self.click_element(self.apply_btn)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
