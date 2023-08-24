""" DominoShowYourWork.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoShowYourWork(BaseFactory):
    """class: DominoShowYourWork"""

    PAGE_URL = "/#/"
    intercom_iframe = '#intercom-frame'
    analysis_details_header = (By.CSS_SELECTOR, '[data-test-id="ShowYourWorkSidebar"] > :nth-child(1) > div > span')
    show_your_work_location = (By.CSS_SELECTOR, '[data-test-id="ShowYourWorkSidebar-locationInfo"]')
    show_your_work_overview = (By.CSS_SELECTOR, '[data-test-id="SYWOverview"]')
    show_your_work_navigation = (By.CSS_SELECTOR, '[data-test-id="ShowYourWorkSidebar-nav"]')
    building = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-structure"]')
    power = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-power"]')
    community = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-people"]')
    highway = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-highway"]')
    bridge = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-bridge"]')
    airport = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-airport"]')
    port = (By.CSS_SELECTOR, '[data-test-id="SYWNavItem-port"]')

    side_panel_wrapper = (By.CSS_SELECTOR, '[data-test-id="SidePanel-Wrapper"]')
    syw_downtime_lifelines = (By.CSS_SELECTOR, '[data-test-id="Lifelines-DataTable-downtimeLifelines"]')
    flood_bridge_lifeline = (By.CSS_SELECTOR, 'tr:nth-child(4) > td:nth-child(1) > div > span')
    wind_bridge_lifeline = (By.CSS_SELECTOR, 'tr:nth-child(6) > td:nth-child(1) > div')

    flood_community_lifeline = (By.CSS_SELECTOR, 'div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div')
    flood_ports_lifeline = (By.CSS_SELECTOR, 'div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(1) > div > span')
    flood_highway_lifeline = (By.CSS_SELECTOR, 'div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(1) > div')

    ### Return Period Chart
    flood_community_return_period_chart = (By.CSS_SELECTOR, '[data-test-id="ReturnPeriodChart-people"]')
    flood_highway_return_period_chart = (By.CSS_SELECTOR, '[data-test-id="ReturnPeriodChart-highway"]')
    earthquake_airport_return_period_chart = (By.CSS_SELECTOR, '[data-test-id="ReturnPeriodChart-airport"]')

    ### Bridge disclaimer
    bridge_disclaimer = (By.CSS_SELECTOR, '[data-test-id="Bridge-FloodWind-disclaimer"]')

    ### Lifelines
    earthquake_bridge_lifeline = (By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(1) > div > span')
    earthquake_bridge_downtime = (By.CSS_SELECTOR, '#bridge-section-detail > p:nth-child(6)')
    earthquake_airport_lifeline = (By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(1) > div > span')
    earthquake_airport_downtime = (By.CSS_SELECTOR, '#airport-section-detail > p:nth-child(6)')

    ### Top3 tables
    bridge_top3_table = (By.CSS_SELECTOR,'#people-section-detail > '
                                         'div.MuiTableContainer-root.jss624.jss627.css-kge0eu > table')
    community_top3_table = (By.CSS_SELECTOR, '[data-test-id="SYWPeople-top3-table"]')
    ports_top3_table = (By.CSS_SELECTOR,'[data-test-id="SYWPort-top3-table"]')
    airport_top3_table = (By.CSS_SELECTOR, '[data-test-id="SYWAirport-top3-table"]')
    highway_top3_table = (By.CSS_SELECTOR,'[data-test-id="SYWHighway-top3-table"]')

    top_concerns_community_downtime = (By.CSS_SELECTOR, 'div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    top_concerns_community_threshold = (By.CSS_SELECTOR, 'div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(3)')
    syw_community_downtime = (By.CSS_SELECTOR, '[data-test-id="SYWPeople-mean"]')
    syw_community_threshold = (By.CSS_SELECTOR, '#people-section-detail > p:nth-child(5)')
    syw_community_range = (By.CSS_SELECTOR, '[data-test-id="downtimeRange"]')


    def assert_show_your_work_report(self):
        """Method: assert_show_your_work_report"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.analysis_details_header)
            assert self.is_element_displayed(self.show_your_work_location) is True, "Missing SYW location info!"
            assert self.is_element_displayed(self.show_your_work_overview) is True, "Missing SYW report!"
            assert self.is_element_displayed(self.show_your_work_navigation) is True, "Missing SYW navigation!"
            assert self.is_element_displayed(self.building) is True, "Missing building lifeline!"
            assert self.is_element_displayed(self.power) is True, "Missing power lifeline!"
            assert self.is_element_displayed(self.community) is True, "Missing community lifeline!"
            assert self.is_element_displayed(self.highway) is True, "Missing highway lifeline!"
            assert self.is_element_displayed(self.bridge) is True, "Missing bridge lifeline!"
            assert self.is_element_displayed(self.airport) is True, "Missing airport lifeline!"
            assert self.is_element_displayed(self.port) is True, "Missing port lifeline!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_side_bar_links(self):
        """Method: click_side_bar_links"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.building)
            self.click_element(self.power)
            self.click_element(self.community)
            self.click_element(self.highway)
            self.click_element(self.bridge)
            self.click_element(self.airport)
            self.click_element(self.port)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_bridge_side_bar_link(self):
        """Method: click_bridge_side_bar_link"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.bridge)
            self.click_element(self.bridge)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_flood_bridge_lifeline(self):
        """Method: click_flood_bridge_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.flood_bridge_lifeline)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_flood_community_lifeline(self):
        """Method: click_flood_community_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.flood_community_lifeline)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_flood_highway_lifeline(self):
        """Method: click_flood_highway_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.flood_highway_lifeline)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_wind_bridge_lifeline(self):
        """Method: click_wind_bridge_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.wind_bridge_lifeline)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_earthquake_bridge_lifeline(self):
        """Method: click_earthquake_bridge_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.earthquake_bridge_lifeline)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_earthquake_airport_lifeline(self):
        """Method: click_earthquake_airport_lifeline"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.earthquake_airport_lifeline)
            self.pause(1)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_bridge_downtime(self):
        """Method: assert_bridge_downtime"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.bridge_disclaimer)
            self.pause(1)
            bridge_disclaimer_text = self.get_text_from_element(self.bridge_disclaimer)
            expected_text = "*Bridge downtime currently applies to earthquake hazards only. Our research indicates " \
                            "that bridges are not susceptible to wind hazards. For floods, since inundation is not a " \
                            "factor due to the space under most bridges, we do not consider them susceptible to flood hazards."
            print(f"Got bridge disclaimer text: {bridge_disclaimer_text}")
            assert bridge_disclaimer_text == expected_text, "Wrong bridge disclaimer found!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_earthquake_bridge_downtime(self):
        """Method: assert_earthquake_bridge_downtime"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.earthquake_bridge_downtime)
            bridge_downtime_text = self.get_text_from_element(self.earthquake_bridge_downtime)
            expected_text = "Our bridge analysis estimates the duration of closures for bridges " \
                    "near the selected location (i.e., within 10 miles) due to bridge damage."
            print(f"Got bridge downtime text: {bridge_downtime_text}")
            assert bridge_downtime_text == expected_text, "Wrong bridge downtime text found!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_earthquake_airport_downtime(self):
        """Method: assert_earthquake_airport_downtime"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.earthquake_airport_downtime)
            airport_downtime_text = self.get_text_from_element(self.earthquake_airport_downtime)
            expected_text = "Our airport analysis estimates the duration of airport closures "\
                            "within 50 miles radius of the selected location."
            print(f"Got airport downtime text: {airport_downtime_text}")
            assert airport_downtime_text == expected_text, "Wrong airport downtime text found!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_flood_community(self):
        """Method: assert_flood_community"""
        try:
            test = inspect.stack()[0][3]
            community_lifeline_downtime_location_detail = self.get_text_from_element(self.top_concerns_community_downtime)
            print(f"Community Location Details Downtime: {community_lifeline_downtime_location_detail}")

            community_lifeline_threshold_location_details = self.get_text_from_element(self.top_concerns_community_threshold)
            print(f"Community Location Details Threshold: {community_lifeline_threshold_location_details}")
            community_threshold_num = self.extract_num(community_lifeline_threshold_location_details)

            self.click_flood_community_lifeline()
            self.pause(1)

            syw_community_downtime_text = self.get_text_from_element(self.syw_community_downtime)
            print(f"SYW Community Downtime: {syw_community_downtime_text}")
            syw_community_threshold_text = self.get_text_from_element(self.syw_community_threshold)
            print(f"SYW Community Threshold: {syw_community_threshold_text}")
            syw_community_threshold_num = self.extract_num(syw_community_threshold_text)
            assert community_lifeline_downtime_location_detail == syw_community_downtime_text, "Miscompare with " \
                                                                                               "community downtime!"
            assert community_threshold_num == syw_community_threshold_num, "Miscompare with community threshold!"
            syw_community_range_text = self.get_text_from_element(self.syw_community_range)
            print(f"SYW Community Range: {syw_community_range_text}")

            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def get_community_downtime(self):
        """Method: get_community_downtime """
        try:
            test = inspect.stack()[0][3]
            downtime_value = self.get_text_from_element(self.syw_community_downtime)
            print(f"Got Community Downtime value: {downtime_value}")
            self.scroll_to_view(self.community_top3_table)
            self.pause(3)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_flood_community_top3_table(self):
        """Method: assert_flood_community_top3_table"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.community_top3_table)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_flood_highway_top3_table(self):
        """Method: assert_flood_highway_top3_table"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.highway_top3_table)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_flood_community_return_period_chart(self):
        """Method: assert_flood_community_return_period_chart"""
        try:
            test = inspect.stack()[0][3]
            self.scroll_to_view(self.flood_community_return_period_chart)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_flood_highway_return_period_chart(self):
        """Method: assert_flood_highway_return_period_chart"""
        try:
            test = inspect.stack()[0][3]
            self.scroll_to_view(self.flood_highway_return_period_chart)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_earthquake_airport_return_period_chart(self):
        """Method: assert_earthquake_airport_return_period_chart"""
        try:
            test = inspect.stack()[0][3]
            self.scroll_to_view(self.earthquake_airport_return_period_chart)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_earthquake_airport_top3_table(self):
        """Method: assert_earthquake_airport_top3_table"""
        try:
            test = inspect.stack()[0][3]
            self.scroll_to_view(self.airport_top3_table)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")
