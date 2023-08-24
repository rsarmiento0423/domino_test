""" DominoROIAnalysis.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoROIAnalysis(BaseFactory):
    """class: DominoROIAnalysis"""

    PAGE_URL = "/#/"
    power_roi_notification = (By.CSS_SELECTOR, '[data-test-id="PowerROI-Notification"]')
    power_roi_modal = (By.CSS_SELECTOR, '[data-test-id="ROIModal"]')
    power_downtime_mitigation_header = (
        By.XPATH,
        "//*[contains(text(), 'Power downtime mitigation')]",
    )
    power_roi_help_article = (By.XPATH, "//span/a[contains(text(), 'What')]")
    roi_analysis_assumptions_header = (
        By.XPATH,
        "//*[contains(text(), 'ROI Analysis Assumptions')]",
    )
    roi_analysis_summary_header = (
        By.XPATH,
        "//*[contains(text(), 'ROI Analysis Summary')]",
    )
    power_downtime_mitigation_suggestions_header = (
        By.XPATH,
        "//*[contains(text(), 'Power Downtime Mitigation Suggestions')]",
    )

    def click_power_roi_notification(self):
        """Method: click_power_roi_notification"""
        try:
            test = inspect.stack()[0][3]
            if self.get_roi_status():
                self.wait_for_element_present(self.power_roi_notification, 60)
                self.click_element(self.power_roi_notification)
                assert self.is_element_present(
                    self.power_roi_modal
                ), "Missing Power ROI Modal!"
                self.wait_for_element_present(self.power_downtime_mitigation_header, 60)
                actual_header = self.get_text_from_element(
                    (self.power_downtime_mitigation_header)
                )
                print(f"Got Power downtime mitigation header: {actual_header}")
                assert (
                    actual_header == "Power downtime mitigation"
                ), "Wrong power downtime mitigation header found!"
            else:
                print(
                    "Skip click_power_roi_notification due to ROI Analysis is disabled!"
                )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_power_roi_analysis_headers(self):
        """Method: assert_power_roi_analysis_headers"""
        try:
            test = inspect.stack()[0][3]
            if self.get_roi_status():
                self.wait_for_element_present(self.power_downtime_mitigation_header, 60)
                assert self.wait_for_element_visible(
                    self.roi_analysis_assumptions_header, 60
                ), "Missing ROI Analysis Assumptions header!"
                assert self.wait_for_element_visible(
                    self.roi_analysis_summary_header, 60
                ), "Missing ROI Analysis Summary header!"
                assert self.wait_for_element_visible(
                    self.power_downtime_mitigation_suggestions_header, 60
                ), "Missing Power Downtime Mitigation Suggestions header!"
            else:
                print(
                    "Skip assert_power_roi_analysis_header due to ROI Analysis is disabled!"
                )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_roi_analysis_help(self):
        """Method: click_roi_analysis_help"""
        try:
            test = inspect.stack()[0][3]
            if self.get_roi_status():
                self.wait_for_element_present(self.power_roi_help_article, 60)
                self.click_element(self.power_roi_help_article)
                lst_win_handles = self.browser.window_handles
                assert (
                    len(lst_win_handles) > 1
                ), "ROI Analysis Help not opened after clicking 'What's this?'!"
                for win_handle in lst_win_handles:
                    self.browser.switch_to.window(win_handle)
                actual_url = self.get_current_url()
                print(f"Got ROI Analysis URL: {actual_url}")
                assert "articles/7992829" in actual_url, "Wrong ROI Analysis URL found!"
            else:
                print("Skip click_roi_analysis_help due to ROI Analysis is disabled!")
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")
