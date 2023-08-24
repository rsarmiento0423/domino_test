""" DominoAnalysisLocationDetailsPage.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoAnalysisLocationDetailsPage(BaseFactory):
    """class: DominoAnalysisLocationDetailsPage"""

    PAGE_URL = "/#/"
    life_lines = [
        "Power",
        "Community",
        "Port",
        "Airport",
        "Bridge*",
        "Highway",
        "Building",
    ]
    download_csv_button = (
        By.CSS_SELECTOR,
        '[data-test-id="vulnerable-locations-list"] [data-test-id="DownloadToCSV"]',
    )
    at_risk_locations_title = (
        By.CSS_SELECTOR,
        '[data-test-id="vulnerable-locations-list"] [data-test-id="VulnerableLocationsList-title"]',
    )
    vulnerable_locations_total = (
        By.CSS_SELECTOR,
        '[data-test-id="VulnerableLocations-loc-count"]',
    )
    show_more_locations_button = (
        By.CSS_SELECTOR,
        '[data-test-id="MoreLocationsButton"]',
    )
    first_at_risk_location = (
        By.CSS_SELECTOR,
        '[data-test-id="VulnerableLocationsList-content"]  .MuiMenuItem-root:nth-child(1)',
    )
    first_at_risk_location_name = (
        By.XPATH,
        '//*[@id="SidePanel-Wrapper"]//ul/li[1]/div[2]/p',
    )
    first_at_risk_location_address = (
        By.XPATH,
        '//*[@id="SidePanel-Wrapper"]//ul/li[1]/div[2]/div',
    )
    tenth_at_risk_location = (
        By.CSS_SELECTOR,
        '[data-test-id="VulnerableLocationsList-content"]  .MuiMenuItem-root:nth-child(19)',
    )
    vulnerable_locations_list_content = (
        By.CSS_SELECTOR,
        '[data-test-id="SidePanel-Wrapper"] [data-test-id="VulnerableLocationsList-content"]',
    )
    update_results_button = (By.CSS_SELECTOR, '[data-test-id="UpdateResultsButton"]')
    learn_more_button = (By.XPATH, "//a[normalize-space()='Learn More']")
    location_name_details_page = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationDetailCard"] h2',
    )
    location_address_details_page = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationDetailCard"] .MuiGrid-item:nth-child(1)',
    )
    chip_location = (By.XPATH, "//div[normalize-space()='At-risk location']")
    back_arrow_button = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationDetailCard"]  .MuiButton-root',
    )
    location_details_header_card = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationDetailCard"]  .MuiCardHeader-root',
    )
    At_risk_title = (By.XPATH, "//h4[normalize-space()='At risk']")
    top_concerns_tab = (By.CSS_SELECTOR, '[data-test-id$="Tab-0"]')
    stress_test_tab = (By.CSS_SELECTOR, '[data-test-id$="Tab-1"]')
    lifeline_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="lifeline-tbl-header-Lifeline"]',
    )
    downtime_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="lifeline-tbl-header-Downtime"]',
    )
    threshold_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="lifeline-tbl-header-Threshold"]',
    )
    lifelines_table = (
        By.CSS_SELECTOR,
        '[data-test-id="Lifelines-DataTable-downtimeLifelines"] .MuiTableBody-root ',
    )
    climate_toggle = (By.CSS_SELECTOR, '[data-test-id="climate-toggle-switch"]')
    downtime_lifeline_tags = (By.CSS_SELECTOR, '[data-test-id="LifelineTag-Caption"]')
    scale_control_txt = (By.CSS_SELECTOR, '[data-test-id="CustomScaleControl-text"]')
    scale_control_scale = (By.CSS_SELECTOR, '[data-test-id="CustomScaleControl-scale"]')
    snack_bar_error_message = (By.CSS_SELECTOR, '[data-test-id="snackbar-title"]')
    snack_bar_dismiss_button = (
        By.CSS_SELECTOR,
        '[data-test-id="snackbar-dismiss-button"]',
    )
    no_at_risk_locations = (
        By.CSS_SELECTOR,
        '[data-test-id="NoLocationDataFoundDescription"]',
    )
    zoom_in = (By.CSS_SELECTOR, "#zoomIn")
    zoom_out = (By.CSS_SELECTOR, "#zoomOut")
    maps_bound_button = (By.CSS_SELECTOR, '[data-test-id="MapBoundsButton"]')
    show_more_locations_button = (
        By.CSS_SELECTOR,
        '[data-test-id="MoreLocationsButton"]',
    )
    building_lifeline = (
        By.CSS_SELECTOR,
        '[data-test-id="Lifelines-DataTable-firstToFail"] > tbody > tr[class="MuiTableRow-root css-1rgksog"]:nth-child(1)',
    )
    all_lifelines = (
        By.CSS_SELECTOR,
        '[data-test-id="Lifelines-DataTable-firstToFail"] > tbody > tr[class="MuiTableRow-root css-1rgksog"] [data-test-id="tableCell-value-lifeline"] > div > span',
    )
    show_your_work_header = (
        By.CSS_SELECTOR,
        '[data-test-id="SYWStructure"] > p:nth-child(1)',
    )
    all_top_concerns_lifelines_labels = (
        By.CSS_SELECTOR,
        'tr > td > div > [data-test-id="LifelineTag-Caption"]',
    )
    all_top_concerns_downtimes = (
        By.CSS_SELECTOR,
        'tr > [data-test-id="tableCell-value-downtime"]',
    )
    all_top_concerns_thresholds = (
        By.CSS_SELECTOR,
        'tr > [data-test-id="tableCell-value-threshold"]',
    )
    top_concerns_community_lifeline_cell = (
        By.CSS_SELECTOR,
        '[data-test-id="Lifelines-DataTable-downtimeLifelines"] > tbody > tr:nth-child(1) > [data-test-id="tableCell-value-lifeline"]',
    )
    top_concerns_community_downtime_header = (
        By.CSS_SELECTOR,
        '[data-test-id="SYWPeople"] > p',
    )
    building_with_different_address = (
        By.CSS_SELECTOR,
        '[data-test-id="builtObject-doesnt-match-location-warning"] > div',
    )
    community_recovery_curve_chart = (
        By.CSS_SELECTOR,
        '[data-test-id="ReturnPeriodChart-people"]',
    )

    def make_sure_some_controls_are_displayed_in_at_risk_list(self):
        """Method: make_sure_some_controls_are_displayed_in_at_risk_list"""
        try:
            test = inspect.stack()[0][3]
            assert self.is_element_displayed(
                self.at_risk_locations_title
            ), "Could not find At-risk locations!"
            assert self.is_element_displayed(
                self.vulnerable_locations_list_content
            ), "Could not find At-risk location list!"
            assert self.is_element_displayed(
                self.show_more_locations_button
            ), "Could not find show more locations button!"
            assert self.is_element_displayed(
                self.first_at_risk_location
            ), "Could not find first At-risk location!"
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def vulnerable_locations_should_be_correct_on_at_risk_table(
        self, number_of_locations
    ):
        """Method: vulnerable_locations_should_be_correct_on_at_risk_table"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.vulnerable_locations_total, 120)
            self.wait_for_element_visible(self.vulnerable_locations_total, 120)
            locations_number = int(
                self.get_text_from_element(self.vulnerable_locations_total).strip(
                    " at risk"
                )
            )
            assert locations_number == int(number_of_locations)
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_on_show_more_button(self):
        """Method: click_on_show_more_button"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.show_more_locations_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def check_show_more_button_shows_the_rest_of_vulnerable_locations(self):
        """Method: check_show_more_button_shows_the_rest_of_vulnerable_locations"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.tenth_at_risk_location)
            assert self.is_element_displayed(
                self.show_more_locations_button
            ), "Show more locations button not found!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_on_first_at_risk_location_card(self):
        """Method: click_on_first_at_risk_location_card"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.first_at_risk_location)
            self.wait_for_element_present(self.learn_more_button, 100)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def check_some_controls_should_displayed_in_the_location_details_page(self):
        """Method: check_some_controls_should_displayed_in_the_location_details_page"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.top_concerns_tab, 100)
            assert self.is_element_displayed(
                self.chip_location
            ), "Chip location not found!"
            assert self.is_element_displayed(
                self.back_arrow_button
            ), "Back arrow button not found!"
            assert self.is_element_displayed(
                self.location_details_header_card
            ), "Location details header card not found!"
            assert self.is_element_displayed(
                self.At_risk_title
            ), "At-risk title not found!"
            assert self.is_element_displayed(
                self.top_concerns_tab
            ), "Top concerns tab not found!"
            assert self.is_element_displayed(
                self.lifeline_table_header
            ), "Lifeline table header not found!"
            assert self.is_element_displayed(
                self.downtime_table_header
            ), "Downtime table header not found!"
            assert self.is_element_displayed(
                self.threshold_table_header
            ), "Threshold table header not found!"
            assert self.is_element_displayed(
                self.lifelines_table
            ), "Lifelines table not found!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def check_location_name_and_address_are_displayed_in_the_details_page(self):
        """Method: check_location_name_and_address_are_displayed_in_the_details_page"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_visible(self.vulnerable_locations_total, 100)
            self.wait_for_element_present(self.vulnerable_locations_total, 100)
            self.wait_for_element_present(self.first_at_risk_location, 100)
            self.wait_for_element_visible(self.first_at_risk_location, 100)
            location_name = self.get_text_from_element(self.first_at_risk_location_name)
            location_address = self.get_text_from_element(
                self.first_at_risk_location_address
            )
            self.click_on_first_at_risk_location_card()
            self.wait_for_element_visible(self.top_concerns_tab, 100)
            location_name_details_page = self.get_text_from_element(
                self.location_name_details_page
            )
            location_address_details_page = self.get_text_from_element(
                self.location_address_details_page
            )
            assert (
                location_name.casefold() in location_name_details_page.casefold()
            ) is True
            assert (
                location_address.casefold() in location_address_details_page.casefold()
            ) is True
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_back_button_from_location_details_page(self):
        """Method: click_back_button_from_location_details_page"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.back_arrow_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_zoom_out_button(self):
        """Method: click_zoom_out_button"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.zoom_out)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_zoom_in_button(self):
        """Method: click_zoom_in_button"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.zoom_in)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_update_results_button(self):
        """Method: click_update_results_button"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.update_results_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_center_map(self):
        """Method: click_center_map"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.click_element(self.maps_bound_button)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def check_map_scale_control_value(self, expected_scale_control_txt):
        """Method: check_map_scale_control_value"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            assert (
                self.wait_for_text_to_be_present(
                    self.scale_control_txt, expected_scale_control_txt, 60
                )
                is True
            ), "Mismatch in map scale!"
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_side_nav_objects(self):
        """Method: assert_side_nav_objects"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.stress_test_tab, 30)
            self.click_element(self.top_concerns_tab)
            matched_lifelines = [
                el.text
                for el in self.browser.find_elements(*self.downtime_lifeline_tags)
            ]
            assert set(matched_lifelines) == set(self.life_lines)
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_side_nav_objects_based_on_cs_admin_configurations(self, entitlements):
        """Method: assert_side_nav_objects_based_on_cs_admin_configurations"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.stress_test_tab, 30)
            self.click_element(self.top_concerns_tab)
            matched_lifelines = [
                el.text
                for el in self.browser.find_elements(*self.downtime_lifeline_tags)
            ]
            assert set(matched_lifelines) == set(
                entitlements
            ), f"Expected {entitlements}, but got {matched_lifelines}"
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_no_at_risk_locations(self):
        """Method: assert_no_at_risk_locations"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.snack_bar_error_message)
            self.click_element(self.snack_bar_dismiss_button)
            assert (
                self.wait_for_element_visible(self.no_at_risk_locations, 60) is True
            ), "Expected 'No at-risk locations'!"
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_learn_more_button(self):
        """Method: click_leqrn_more_button"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.learn_more_button)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_locations_details_card(self):
        """Method:"""
        try:
            test = inspect.stack()[0][3]
            self.is_element_displayed(self.location_address_details_page, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_show_more_locations_button(self):
        """Method: click_show_more_locations_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.show_more_locations_button, 60)
            self.click_element(self.show_more_locations_button, 60)
            if self.is_element_displayed(self.show_more_locations_button):
                self.click_show_more_locations_button()
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_top_concerns_tab(self):
        """Method: click_top_concerns_tab"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.top_concerns_tab, 60)
            self.click_element(self.top_concerns_tab, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_stress_tab(self):
        """Method: click_stress_tab"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.stress_test_tab, 60)
            self.click_element(self.stress_test_tab, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_all_lifelines(self):
        """Method: assert_all_lifelines"""
        try:
            test = inspect.stack()[0][3]
            actual_lifelines = []
            expected_lifelines = [
                "Building",
                "Power",
                "Highway",
                "Community",
                "Bridge*",
                "Port",
                "Airport",
            ]
            self.wait_for_element_present(self.all_lifelines, 60)
            lifelines = self.get_number_of_elements(self.all_lifelines)
            assert len(lifelines) == 7, f"Expected 7, got {len(lifelines)} lifelines!"
            for lifeline in lifelines:
                lifeline_name = lifeline.text
                print(f"Lifeline: {lifeline_name}")
                actual_lifelines.append(lifeline_name)
            assert actual_lifelines == expected_lifelines, "Wrong lifelines displayed!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_show_your_work_building_lifeline(self):
        """Method: assert_show_your_work_building_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.building_lifeline, 60)
            self.click_element(self.building_lifeline, 60)
            self.wait_for_element_present(self.show_your_work_header)
            actual = self.get_text_from_element(self.show_your_work_header)
            print(f"Got Show Your Work header: {actual}")
            expected = "Building damage"
            assert actual == expected, f"Expected: {expected} lifeline header!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def get_top_concerns_data(self):
        """Method: get_top_concerns_data"""
        try:
            test = inspect.stack()[0][3]
            # Lifelines
            expected_lifelines = [
                "Community",
                "Power",
                "Highway",
                "Bridge*",
                "Port",
                "Airport",
                "Building",
            ]
            self.wait_for_element_present(self.all_top_concerns_lifelines_labels, 60)
            top_concerns_lifelines = self.get_number_of_elements(
                self.all_top_concerns_lifelines_labels
            )
            assert len(top_concerns_lifelines) == 7, (
                f"Expected 7, got {len(top_concerns_lifelines)} top "
                f"concerns lifelines!"
            )

            actual_top_concerns_lifelines = self.get_element_values(
                top_concerns_lifelines
            )
            print(f"Lifelines: {actual_top_concerns_lifelines}")
            assert (
                actual_top_concerns_lifelines == expected_lifelines
            ), "Wrong top concerns lifelines displayed!"

            # Downtime
            self.wait_for_element_present(self.all_top_concerns_downtimes, 60)
            top_concerns_downtimes = self.get_number_of_elements(
                self.all_top_concerns_downtimes
            )
            actual_top_concerns_downtimes = self.get_element_values(
                top_concerns_downtimes
            )
            print(f"Downtimes: {actual_top_concerns_downtimes}")

            descending_flag = 0
            i = 1
            while i < len(actual_top_concerns_downtimes):
                if (
                    actual_top_concerns_downtimes[i]
                    >= actual_top_concerns_downtimes[i - 1]
                ):
                    descending_flag = 1
                i += 1
            assert descending_flag, "Downtimes NOT in descending order!"

            # Threshold
            self.wait_for_element_present(self.all_top_concerns_thresholds, 60)
            top_concerns_thresholds = self.get_number_of_elements(
                self.all_top_concerns_thresholds
            )
            actual_top_concerns_thresholds = self.get_element_values(
                top_concerns_thresholds
            )
            print(f"Thresholds: {actual_top_concerns_thresholds}")
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_top_concerns_community(self):
        """Method: click_top_concerns_community"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.top_concerns_community_lifeline_cell, 60)
            self.click_element(self.top_concerns_community_lifeline_cell, 60)
            self.wait_for_element_present(
                self.top_concerns_community_downtime_header, 60
            )
            actual = self.get_text_from_element(
                self.top_concerns_community_downtime_header
            )
            print(f"Got Show Your Work header: {actual}")
            expected = "Community downtime"
            assert actual == expected, f"Expected: {expected} lifeline header!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_community_recovery_curve_chart(self):
        """Method: assert_community_recovery_curve_chart"""
        try:
            test = inspect.stack()[0][3]
            assert self.is_element_present(self.community_recovery_curve_chart), (
                "Missing Community Recovery Curve " "Chart!"
            )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_address_no_match(self):
        """Method: assert_address_no_match"""
        try:
            test = inspect.stack()[0][3]
            assert self.is_element_present(self.building_with_different_address), (
                "Expected different address match " "not found!"
            )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")
