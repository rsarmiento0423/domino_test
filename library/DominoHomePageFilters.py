""" DominoHomePageFilters.py """
import inspect
from BaseFactory import *
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


class DominoHomePageFilters(BaseFactory):
    """class: DominoHomePageFilters"""

    path = "/#/"
    user_profile = (By.CSS_SELECTOR, '[data-test-id="user-profile"]')
    climate_toggle = (By.CSS_SELECTOR, '[data-test-id="climate-toggle-switch"]')
    climate_toggle_label = (By.CSS_SELECTOR, '[data-test-id="climate-toggle-label"]')
    thresholds_picker_button = (
        By.CSS_SELECTOR,
        '[data-test-id="thresholds-picker-button"]',
    )
    hazard_filter_button = (
        By.CSS_SELECTOR,
        '[data-test-id="primary-nav"]  .MuiButton-root',
    )
    return_period_button = (
        By.CSS_SELECTOR,
        '[data-test-id="PLANNING_HORIZON-picker-button"]',
    )
    locations_picker_form = (By.CSS_SELECTOR, '[data-test-id="locations-PickerForm"]')
    location_search_input = (By.ID, "location-autocomplete-search")
    Search_button = (
        By.CSS_SELECTOR,
        '[data-test-id="app-nav"] .MuiInputAdornment-root',
    )
    intercom_messenger = (By.CSS_SELECTOR, '[data-test-id="IntercomButton"]')
    at_risk_locations_side_panel = (
        By.CSS_SELECTOR,
        '[data-test-id="SidePanel-Wrapper"]',
    )
    thresholds_help = (By.CSS_SELECTOR, '[data-test-id="threshold-help-cell"]')
    threshold_building_structuralDamage_input = (
        By.CSS_SELECTOR,
        '[data-test-id="PercentInput-structuralDamage"]',
    )
    threshold_powerDowntime_days = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-days-powerDowntime"]',
    )
    threshold_powerDowntime_hours = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-hours-powerDowntime"]',
    )
    threshold_peopleDowntime_days = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-days-peopleDowntime"]',
    )
    threshold_peopleDowntime_hours = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-hours-peopleDowntime"]',
    )
    threshold_highwayDowntime_days = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-days-highwayDowntime"]',
    )
    threshold_highwayDowntime_hours = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-hours-highwayDowntime"]',
    )
    threshold_bridgeDowntime_days = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-days-bridgeDowntime"]',
    )
    threshold_bridgeDowntime_hours = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-hours-bridgeDowntime"]',
    )
    threshold_portDowntime_days = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-days-portDowntime"]',
    )
    threshold_portDowntime_hours = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-hours-portDowntime"]',
    )
    threshold_airportDowntime_days = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-days-airportDowntime"]',
    )
    threshold_airportDowntime_hours = (
        By.CSS_SELECTOR,
        '[data-test-id="DaysHoursInput-hours-airportDowntime"]',
    )
    threshold_resetToDefaults_button = (
        By.CSS_SELECTOR,
        '[data-test-id="thresholds-PickerForm-form"] .MuiButton-root:nth-child(1)',
    )
    threshold_cancel_button = (By.NAME, "cancel")
    threshold_apply_button = (By.NAME, "apply")
    hazard_menu = (
        By.CSS_SELECTOR,
        '[data-test-id="HazardSelector-menu"]  .MuiPaper-root',
    )
    hazard_selector_flood_row = (
        By.CSS_SELECTOR,
        '[data-test-id="HazardSelector-menu"] .MuiMenuItem-root:nth-child(1)',
    )
    hazard_selector_wind_row = (
        By.CSS_SELECTOR,
        '[data-test-id="HazardSelector-menu"] .MuiMenuItem-root:nth-child(2)',
    )
    hazard_selector_earthquake_row = (
        By.CSS_SELECTOR,
        '[data-test-id="HazardSelector-menu"] .MuiMenuItem-root:nth-child(3)',
    )
    map_bound_button = (By.CSS_SELECTOR, '[data-test-id="MapBoundsButton"]')
    icon_1c = (By.CSS_SELECTOR, "#onec-logo > div > a")
    version_info = (By.CSS_SELECTOR, '[data-test-id="version-information"]')
    version_control_header = (By.CSS_SELECTOR, "div.flex.flex-col > header")
    at_risk_side_bar_button = (
        By.CSS_SELECTOR,
        '[data-test-id="vulnerable-locations-list"] > div > div > div > button',
    )
    financial_loss_calculator_side_bar_button = (
        By.CSS_SELECTOR,
        '[data-test-id="materiality-view-container"] > div > button',
    )
    no_data_available_txt = (
        By.CSS_SELECTOR,
        '[data-test-id="materiality-empty-view"] > div > p:nth-child(1)',
    )
    set_up_analysis_txt = (
        By.CSS_SELECTOR,
        '[data-test-id="materiality-empty-view"] > div > p:nth-child(2)',
    )
    set_up_analysis_button = (
        By.CSS_SELECTOR,
        '[data-test-id="get-started-analysis-link"]',
    )
    learn_more_materiality = (By.CSS_SELECTOR, 'a[href="#/materiality"]')
    financial_loss_calculator_help = (By.PARTIAL_LINK_TEXT, "What")

    def open_home_page(self, url):
        """Method: open_home_page"""
        try:
            test = inspect.stack()[0][3]
            self.open(f"{url}{self.path}")
            self.wait_for_element_present(self.user_profile, 60)
            self.wait_for_element_visible(self.user_profile, 60)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def all_filters_on_homepage_should_be_displayed(self):
        """Method: all_filters_on_homepage_should_be_displayed"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.user_profile, 60)
            self.wait_for_element_present(self.at_risk_locations_side_panel, 60)
            self.wait_for_element_present(self.map_bound_button, 60)
            assert (
                self.is_element_displayed(self.climate_toggle) is True
            ), "Issue with toggling Climate"
            assert (
                self.is_element_displayed(self.thresholds_picker_button) is True
            ), "Issue with Thresholds picker!"
            assert (
                self.is_element_displayed(self.hazard_filter_button) is True
            ), "Issue with Hazard filter button!"
            assert (
                self.is_element_displayed(self.return_period_button) is True
            ), "Issue with Return Period button!"
            assert (
                self.is_element_displayed(self.locations_picker_form) is True
            ), "Issue wih Locations Picker!"
            assert (
                self.is_element_displayed(self.location_search_input) is True
            ), "Issue with location search!"
            assert (
                self.is_element_displayed(self.intercom_messenger) is True
            ), "Issue with Intercom Messenger!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def switch_climate_change_filter_on_off(self, climate_status):
        """Method: switch_climate_change_filter_on_off"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.climate_toggle, timeout=30)
            self.pause()
            if self.get_text_from_element(self.climate_toggle_label) != climate_status:
                self.click_element(self.climate_toggle)
                assert (
                    self.get_text_from_element(self.climate_toggle_label)
                    == climate_status
                )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def user_click_on_threshold_filter(self):
        """Method: user_click_on_threshold_filter"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.thresholds_picker_button, timeout=100)
            try:
                self.click_element(self.thresholds_picker_button, timeout=100)
            except StaleElementReferenceException:
                print(
                    "StaleElementReferenceException while trying to click threshold picker, trying to find element again"
                )
                self.click_element(self.thresholds_picker_button, timeout=100)
            time.sleep(1)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def check_all_threshold_filter_input_fields_are_displayed(self):
        """Method: check_all_threshold_filter_input_fields_are_displayed"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.thresholds_help, 30)
            self.wait_for_element_present(
                self.threshold_building_structuralDamage_input, 30
            )
            self.wait_for_element_present(self.threshold_airportDowntime_days, 30)
            assert (
                self.is_element_displayed(self.threshold_airportDowntime_days) is True
            ), "Issue with airport downtime in days!"
            assert (
                self.is_element_displayed(self.threshold_airportDowntime_hours) is True
            ), "Issue with airport downtime in hours!"
            assert (
                self.is_element_displayed(self.threshold_bridgeDowntime_days) is True
            ), "Issue with bridge downtime in days!"
            assert (
                self.is_element_displayed(self.threshold_bridgeDowntime_hours) is True
            ), "Issue with bridge downtime in hour!"
            assert (
                self.is_element_displayed(self.threshold_peopleDowntime_days) is True
            ), "Issue with people downtime in days!"
            assert (
                self.is_element_displayed(self.threshold_peopleDowntime_hours) is True
            ), "Issue with people downtime in hours!"
            assert (
                self.is_element_displayed(self.threshold_highwayDowntime_days) is True
            ), "Issue with highway downtime in days!"
            assert (
                self.is_element_displayed(self.threshold_highwayDowntime_hours) is True
            ), "Issue with highway downtime in hours!"
            assert (
                self.is_element_displayed(self.threshold_portDowntime_days) is True
            ), "Issue with port downtime in days!"
            assert (
                self.is_element_displayed(self.threshold_portDowntime_hours) is True
            ), "Issue with port downtime in hours!"
            assert (
                self.is_element_displayed(self.threshold_powerDowntime_days) is True
            ), "Issue with power downtime in days!"
            assert (
                self.is_element_displayed(self.threshold_powerDowntime_hours) is True
            ), "Issue with power downtime in hours!"
            assert (
                self.is_element_displayed(self.threshold_cancel_button) is True
            ), "Issue with threshold cancel button!"
            assert (
                self.is_element_displayed(self.threshold_apply_button) is True
            ), "Issue with threshold apply button!"
            assert (
                self.is_element_displayed(self.threshold_resetToDefaults_button) is True
            ), "Issue with threshold ResetToDefaults button!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def user_can_edit_the_threshold_building_filter(self, new_value):
        """Method: user_can_edit_the_threshold_building_filter"""
        try:
            test = inspect.stack()[0][3]
            time.sleep(1)
            self.wait_for_element_present(self.thresholds_help, 30)
            self.clear_element_text(self.threshold_building_structuralDamage_input, 10)
            self.send_keys_to_element(
                self.threshold_building_structuralDamage_input, new_value
            )
            self.click_element(self.threshold_apply_button, 10)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def user_check_the_new_buildings_threshold_value(self, new_value):
        """Method: user_check_the_new_buildings_threshold_value"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.thresholds_help, 30)
            assert (
                self.get_attribute_value(self.threshold_building_structuralDamage_input)
                == new_value
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(inspect.stack()[0][3])
            raise AssertionError(f"Failed {test} due to: {error}!")

    def user_to_check_the_default_threshold_filter_values(self):
        """Method: user_to_check_the_default_threshold_filter_values"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.thresholds_help, 30)
            assert (
                self.get_attribute_value(self.threshold_building_structuralDamage_input)
                == "5"
            )
            assert self.get_attribute_value(self.threshold_airportDowntime_days) == "0"
            assert self.get_attribute_value(self.threshold_airportDowntime_hours) == "2"
            assert self.get_attribute_value(self.threshold_bridgeDowntime_days) == "0"
            assert self.get_attribute_value(self.threshold_bridgeDowntime_hours) == "2"
            assert self.get_attribute_value(self.threshold_peopleDowntime_days) == "0"
            assert self.get_attribute_value(self.threshold_peopleDowntime_hours) == "2"
            assert self.get_attribute_value(self.threshold_highwayDowntime_days) == "0"
            assert self.get_attribute_value(self.threshold_highwayDowntime_hours) == "2"
            assert self.get_attribute_value(self.threshold_portDowntime_days) == "0"
            assert self.get_attribute_value(self.threshold_portDowntime_hours) == "2"
            assert self.get_attribute_value(self.threshold_powerDowntime_days) == "0"
            assert self.get_attribute_value(self.threshold_powerDowntime_hours) == "2"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def restore_filters_to_default(self):
        """Method: restore_filters_to_default"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.thresholds_help, 30)
            self.click_element(self.threshold_resetToDefaults_button, 30)
            try:
                self.click_element(self.threshold_apply_button, 30)
            except StaleElementReferenceException:
                print(
                    "StaleElementReferenceException while trying to click apply, trying to find element again"
                )
                self.click_element(self.threshold_apply_button, 30)
            self.wait_for_element_present(self.thresholds_picker_button, 30)
            time.sleep(1)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def user_to_cancel_the_values_changes_in_threshold_filter(self, new_value):
        """Method: user_to_cancel_the_values_changes_in_threshold_filter"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.thresholds_help, 100)
            self.clear_element_text(self.threshold_building_structuralDamage_input, 10)
            self.send_keys_to_element(
                self.threshold_building_structuralDamage_input, new_value
            )
            self.click_element(self.threshold_cancel_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def check_hazard_selector_list_values_for_domino_us(self):
        """Method: check_hazard_selector_list_values_for_domino_us"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.hazard_filter_button, 30)
            time.sleep(5)
            self.click_element(self.hazard_filter_button, 30)
            time.sleep(3)
            assert self.is_element_displayed(self.hazard_selector_flood_row, 10) is True
            assert self.is_element_displayed(self.hazard_selector_wind_row, 10) is True
            assert (
                self.is_element_displayed(self.hazard_selector_earthquake_row, 10)
                is True
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def user_can_choose_different_hazard_types(self):
        """Method: user_can_choose_different_hazard_types"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.hazard_filter_button, 60)
            self.wait_for_element_present(self.at_risk_locations_side_panel, 60)
            self.wait_for_element_present(self.map_bound_button, 60)
            try:
                self.click_element(self.hazard_filter_button, 60)
            except StaleElementReferenceException:
                print(
                    "StaleElementReferenceException while trying to click apply, trying to find element again"
                )
                self.click_element(self.hazard_filter_button)
            self.wait_for_element_present(self.hazard_selector_flood_row, 60)
            # select Earthquake
            self.click_element(self.hazard_selector_earthquake_row, 60)
            time.sleep(2)
            assert self.get_text_from_element(self.hazard_filter_button) == "Earthquake"
            # select the Flood
            self.click_element(self.hazard_filter_button, 60)
            self.wait_for_element_present(self.hazard_selector_flood_row, 60)
            self.click_element(self.hazard_selector_flood_row, 60)
            time.sleep(2)
            assert self.get_text_from_element(self.hazard_filter_button) == "Flood"
            # select the Wind
            self.click_element(self.hazard_filter_button, 60)
            self.wait_for_element_present(self.hazard_selector_flood_row, 60)
            self.click_element(self.hazard_selector_wind_row, 60)
            time.sleep(2)
            assert self.get_text_from_element(self.hazard_filter_button) == "Wind"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def choose_flood(self):
        """Method: choose_flood"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.hazard_filter_button, 60)
            self.wait_for_element_present(self.hazard_selector_flood_row, 60)
            self.click_element(self.hazard_selector_flood_row, 60)
            time.sleep(2)
            assert self.get_text_from_element(self.hazard_filter_button) == "Flood"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def choose_earthquake(self):
        """Method: choose_earthquake"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.hazard_filter_button, 60)
            self.wait_for_element_present(self.hazard_selector_earthquake_row, 60)
            self.click_element(self.hazard_selector_earthquake_row, 60)
            time.sleep(2)
            assert self.get_text_from_element(self.hazard_filter_button) == "Earthquake"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def choose_wind(self):
        """Method: choose_wind"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.hazard_filter_button, 60)
            self.wait_for_element_present(self.hazard_selector_wind_row, 60)
            self.click_element(self.hazard_selector_wind_row, 60)
            time.sleep(2)
            assert self.get_text_from_element(self.hazard_filter_button) == "Wind"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_1c_icon(self):
        """Method: click_1c_icon"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.icon_1c, 60)
            self.click_element(self.icon_1c, 60)
            lst_win_handles = self.browser.window_handles
            assert (
                len(lst_win_handles) > 1
            ), "1C page not opened after clicking 1C logo!"
            for win_handle in lst_win_handles:
                self.browser.switch_to.window(win_handle)
            actual_page_title = self.browser.title
            assert (
                actual_page_title
                in "One Concern | Planetary-Scale Resilience Software Platform"
            ), "Wrong page title found!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_version_link_with_version_control_article(self, country):
        """Method: click_version_link_with_version_control_article"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.version_info, 60)
            version_info_text = self.get_text_from_element(self.version_info)
            print(f"Version Information: {version_info_text}")
            self.click_element(self.version_info, 60)
            self.pause(3)
            if country == "US":
                handles = self.browser.window_handles
                size = len(handles)
                print(f"Total window handles found: {size}")
                parent_handle = self.browser.current_window_handle
                assert (
                    len(handles) > 1
                ), "Version Control article not opened after clicking version info link!"
                for num in range(size):
                    if handles[num] != parent_handle:
                        self.browser.switch_to.window(handles[num])
                        actual_page_title = self.browser.title
                        print(f"Got page title: {actual_page_title}")
                        assert (
                            actual_page_title
                            in "Version Control | One Concern Help Center"
                        ), "Wrong page title found!"
                        break
                version_control_header = self.get_text_from_element(
                    self.version_control_header
                )
                print(f"Got Version Control header: {version_control_header}")
                assert (
                    version_control_header == "Version Control"
                ), "Wrong Version Control header found~"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_at_risk_side_bar(self):
        """Method: click_at_risk_side_bar"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.at_risk_side_bar_button, 60)
            self.click_element(self.at_risk_side_bar_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_financial_losss_calculator_side_bar(self):
        """Method: click_financial_losss_calculator_side_bar"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(
                self.financial_loss_calculator_side_bar_button, 60
            )
            self.click_element(self.financial_loss_calculator_side_bar_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def expand_and_collapse_side_bars(self):
        """Method: expand_and_collapse_side_bars"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.at_risk_side_bar_button, 60)
            self.click_element(self.at_risk_side_bar_button, 60)
            self.pause(1)
            self.click_element(self.at_risk_side_bar_button, 60)
            self.pause(1)
            self.wait_for_element_present(
                self.financial_loss_calculator_side_bar_button, 60
            )
            self.click_element(self.financial_loss_calculator_side_bar_button, 60)
            self.pause(1)
            self.click_element(self.financial_loss_calculator_side_bar_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_no_data_analysis_available(self):
        """Method: assert_no_data_analysis_available"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.set_up_analysis_button, 60)

            actual_no_data_available_txt = self.get_text_from_element(
                self.no_data_available_txt
            )
            assert (
                actual_no_data_available_txt == "No data available."
            ), "Wrong message displayed when no data analysis available!"

            actual_setup_analysis_txt = self.get_text_from_element(
                self.set_up_analysis_txt
            )
            assert (
                actual_setup_analysis_txt == "Click set up analysis to get started."
            ), "Wrong message displayed for setting up analysis!"
            # assert (
            #     self.is_element_displayed(self.set_up_analysis_button),
            #     "'Set Up Analysis' button found not found!",
            # )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_setup_analysis_button(self):
        """Method: click_setup_analysis_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.set_up_analysis_button, 60)
            self.click_element(self.set_up_analysis_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_learn_more_materiality_button(self):
        """Method: click_learn_more_materiality_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.learn_more_materiality, 60)
            self.click_element(self.learn_more_materiality, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_sidebar_flc_help_link(self):
        """Method: click_sidebar_flc_help_link"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.financial_loss_calculator_help, 60)
            self.click_element(self.financial_loss_calculator_help, 60)
            lst_win_handles = self.browser.window_handles
            assert (
                len(lst_win_handles) > 1
            ), "Financial Loss Calculate Help not opened after clicking 'Whats this?'!"
            for win_handle in lst_win_handles:
                self.browser.switch_to.window(win_handle)
            actual_url = self.get_current_url()
            print(f"Got Financial Loss Calculator URL: {actual_url}")
            assert "articles/6950409-financial-loss-calculator" in actual_url, \
                "Wrong Financial Loss URL found!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")
