""" DominoSearchField.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoSearchField(BaseFactory):
    """class: DominoSearchField"""

    PAGE_URL = "/#/"

    location_search_input = (
        By.CSS_SELECTOR,
        '[data-test-id="app-nav"] [id="location-autocomplete-search"]',
    )
    user_profile_button = (
        By.CSS_SELECTOR,
        '[data-test-id="user-profile"]',
    )
    planning_horizon = (
        By.CSS_SELECTOR,
        '[data-test-id="PLANNING_HORIZON-PickerForm"]',
    )
    Threshold_dropdown = (
        By.CSS_SELECTOR,
        '[data-test-id="picker-button-maintext"]',
    )
    search_button = (
        By.CSS_SELECTOR,
        '[data-test-id="app-nav"] .MuiInputAdornment-root',
    )
    location_counts = (
        By.CSS_SELECTOR,
        '[data-test-id="vll-location-counts-container"]',
    )
    search_result0 = (By.ID, "location-autocomplete-search-option-0")
    search_result1 = (By.ID, "location-autocomplete-search-option-1")
    search_result2 = (By.ID, "location-autocomplete-search-option-2")
    search_result3 = (By.ID, "location-autocomplete-search-option-3")
    side_panel_header = (
        By.CSS_SELECTOR,
        '[data-test-id="SidePanel-Wrapper"] [data-test-id="LocationDetailCard"] .MuiTypography-h2',
    )
    atrisk_tab = (
        By.CSS_SELECTOR,
        '[data-test-id="SidePanel-Wrapper"] [data-test-id="LocationDetailCard"] [data-test-id="LocationDetail-content"]',
    )
    no_commercial_building_found = (
        By.CSS_SELECTOR,
        '[data-test-id="NoLocationFound"] > span:nth-child(4)',
    )
    view_3d_diagram = (
        By.CSS_SELECTOR,
        '[data-test-id="viewNavigator"] [data-test-id="navigatorInArc"] [data-test-id="launch"]',
    )
    play_hazard_simultaion = (
        By.CSS_SELECTOR,
        '[data-test-id="viewNavigator"] [data-test-id="navigatorToFirstFail"] > div > [data-test-id="launch"]',
    )
    play_button = (
        By.CSS_SELECTOR,
        '[data-test-id="FirstFailTimeline"] [data-test-id="PlayButton"]',
    )
    location_info_name = (By.CSS_SELECTOR, '[data-test-id="location-info-name"]')
    header_3d_diagram = (By.CSS_SELECTOR, '[data-test-id="header"]')
    symbolic_view = (
        By.CSS_SELECTOR,
        '[data-test-id="Lifeline-Location-Vulnerable-Img"]',
    )
    power_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-power"] > div > svg',
    )
    community_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-people"] > div > svg',
    )
    highway_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-highway"] > div > svg',
    )
    building_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-structure"] > div > svg',
    )
    bridge_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-bridge"] > div > svg',
    )
    airport_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-airport"] > div > svg',
    )
    port_details = (
        By.CSS_SELECTOR,
        '[data-test-id="LifelineVulnerableDetail-port"] > div > svg',
    )
    syw_community_downtime_header = (
        By.CSS_SELECTOR,
        '[data-test-id="SYWPeople"] > p:nth-child(1)',
    )

    def search_for_commercial_building(self, commercialbuilding):
        """Method: search_for_commercial_building"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.user_profile_button, 100)
            self.wait_for_element_present(self.planning_horizon, 100)
            self.wait_for_element_present(self.user_profile_button, 100)
            self.click_element(self.location_search_input)
            self.send_keys_to_element(self.location_search_input, commercialbuilding)
            self.wait_for_element_visible(self.search_result1, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_no_commercial_building(self, commercialbuilding):
        """Method: assert_no_commercial_building"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.location_search_input)
            self.send_keys_to_element(self.location_search_input, commercialbuilding)
            self.wait_for_element_visible(self.search_result1, 60)
            self.click_element(self.search_result1)
            self.wait_for_element_present(self.no_commercial_building_found, 100)
            no_data_found = self.get_text_from_element(
                self.no_commercial_building_found
            )
            print(f"Got message: {no_data_found}!")
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_search_results_related_to_search_criteria(self, searchcriteria):
        """Method: assert_search_results_related_to_search_criteria"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_visible(self.search_result1, 30)
            search_result1 = self.get_text_from_element(self.search_result1)
            print(f"Got location name: {search_result1}!")
            assert (searchcriteria.casefold() in search_result1.casefold()) is True
            search_result2 = self.get_text_from_element(self.search_result2)
            print(f"Got location address: {search_result2}!")
            assert (searchcriteria.casefold() in search_result2.casefold()) is True
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_search_results_related_to_listed_first(self, searchcriteria):
        """Method: assert_search_results_related_to_listed_first"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_visible(self.search_result1, 30)
            search_result = self.get_text_from_element(self.search_result1)
            print(f"Got location name: {search_result}!")
            assert (searchcriteria.casefold() in search_result.casefold()) is True
            self.click_element(self.search_result1)
            self.wait_for_element_present(self.side_panel_header, 30)
            sidepanelheader = self.get_text_from_element(self.side_panel_header)
            print(f"Got location name: {sidepanelheader}!")
            assert (sidepanelheader.casefold() in search_result.casefold()) is True
            assert self.is_element_displayed(self.atrisk_tab) is True
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def search_result(self):
        """Method: search_result"""
        try:
            test = inspect.stack()[0][3]
            searchresult = self.get_text_from_element(self.search_result2)
            print(f"Got location address: {searchresult}!")
            self.click_element(self.search_result2)
            self.wait_for_element_present(self.side_panel_header, 30)
            sidepanelheader = self.get_text_from_element(self.side_panel_header)
            print(f"Got location name: {sidepanelheader}!")
            assert (sidepanelheader.casefold() in searchresult.casefold()) is True
            assert self.is_element_displayed(self.atrisk_tab) is True
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_recently_viewed_location(self, searchlocation):
        """Method: assert_recently_viewed_location"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.location_search_input)
            self.click_element(self.location_search_input)
            self.wait_for_element_visible(self.search_result0, 30)
            search_result = self.get_text_from_element(self.search_result0)
            print(f"Got location name: {search_result}!")
            assert (
                searchlocation.casefold() in search_result.casefold()
            ) is True, f"Should contain: {searchlocation}"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_view_3d_diagram(self):
        """Method: click_view_3d_diagram"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.view_3d_diagram, 60)
            self.click_element(self.view_3d_diagram)
            self.wait_for_element_present(
                self.symbolic_view, 60
            )  # Verify Symbolic View appears
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_play_hazard_simulation(self, location, hazard):
        """Method click_play_hazard_simulation"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.play_hazard_simultaion)
            location_name = self.get_text_from_element(self.location_info_name)
            assert location_name == location, f"Expecting location: {location}!"
            hazard_simulation = self.get_text_from_element(self.header_3d_diagram)
            assert (
                hazard_simulation == hazard
            ), f"Expecting hazard simulation: {hazard}!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_play_button(self):
        """Method: click_play_button"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.play_button)
            self.pause(10)
            self.generate_screenshot(test)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_show_downtime_details_symbolic_view(self):
        """Method: assert_show_downtime_details_symbolic_view"""
        try:
            test = inspect.stack()[0][3]
            assert self.is_element_present(
                self.power_details
            ), "Missing Show details for Power!"
            assert self.is_element_present(
                self.community_details
            ), "Missing Show details for Community!"
            assert self.is_element_present(
                self.highway_details
            ), "Missing Show details for Highway!"
            assert self.is_element_present(
                self.building_details
            ), "Missing Show details for Building!"
            assert self.is_element_present(
                self.bridge_details
            ), "Missing Show details for Bridge!"
            assert self.is_element_present(
                self.airport_details
            ), "Missing Show details for Airport!"
            assert self.is_element_present(
                self.port_details
            ), "Missing Show details for Port!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_community_show_details(self):
        """Method click_community_show_details"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.community_details)
            self.click_element(self.community_details)

            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_show_your_work_community_downtime(self):
        """Method: assert_show_your_work_community_downtime"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.syw_community_downtime_header)
            actual = self.get_text_from_element(self.syw_community_downtime_header)
            print(f"Got Community Downtime header: {actual}")
            expected = "Community downtime"
            assert actual == expected, f"Expected: {expected} header!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")
