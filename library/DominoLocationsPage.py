""" DominoLoginPage.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoLocationsPage(BaseFactory):
    """class: DominoLocationsPage"""

    path = "/#/locations"
    snackbar_title = (By.CSS_SELECTOR, '[data-test-id="snackbar-title"]')
    processed_locations = (By.CSS_SELECTOR, '[data-test-id="numLocationsProcessed"]')
    browse_files_button = (By.CSS_SELECTOR, '[data-test-id="Browse-Files"]')
    snackbar_description = (By.CSS_SELECTOR, '[data-test-id="snackbar-description"]')
    manage_locations = (By.CSS_SELECTOR, '[data-test-id="manage-locations"]')
    at_risk_title = (By.CSS_SELECTOR, '[data-test-id="VulnerableLocationsList-title"]')
    help_link = (By.CSS_SELECTOR, '[data-test-id="HelpLink"]')
    Download_to_csv = (By.CSS_SELECTOR, '[data-test-id="DownloadToCSV"]')
    delete_file_button = (By.CSS_SELECTOR, '[data-test-id="deleteButton"]')
    delete_file_confirmation_button = (
        By.CSS_SELECTOR,
        '[data-test-id="noBackupButton"]',
    )
    delete_file_cancel_button = (By.CSS_SELECTOR, '[data-test-id="cancelButton"]')
    delete_file_backup_and_delete = (By.CSS_SELECTOR, '[data-test-id="backupButton"]')
    locations_processed = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationsCsvDetails-processed"] .MuiTypography-h1',
    )
    upload_files_zone = (
        By.CSS_SELECTOR,
        '[data-test-id="Location-Upload-Dropzone"] input[type="file"]',
    )
    analysis_bar_locations_total = (
        By.CSS_SELECTOR,
        '[data-test-id="TotalLocations-loc-count"]',
    )
    name_header = (By.CSS_SELECTOR, '[data-test-id="PersonalInfo"]')
    error_message_description = (
        By.CSS_SELECTOR,
        '[data-test-id="snackbar-description"]',
    )
    locations_hidden_header = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationsCsvDetails-hidden"] [data-test-id="Callout-info-inline"]',
    )
    locations_hidden_number = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationsCsvDetails-hidden"] h1',
    )
    # add new page elements in Manage locations page in case feature flag is on for Building matching
    delete_without_backup_button = (By.CSS_SELECTOR, '[data-test-id="noBackupButton"]')
    flag_on_locations_processed = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationsCsvStats-Container"]  .MuiTypography-h1',
    )
    flag_on_locations_hidden_number = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationsCsvStats-rejected"] [data-test-id="numLocationsRejected"]',
    )
    last_updated_time = (
        By.CSS_SELECTOR,
        '[data-test-id="LocationsCsvDetails"] [data-test-id="lastUploadedTimeDate"]',
    )
    vulnerable_locations_list = (
        By.CSS_SELECTOR,
        '[data-test-id="VulnerableLocationsList-content"]',
    )
    big_file_uploads_error_message = (
        By.CSS_SELECTOR,
        '[data-test-id="ConfirmDialogDescription"]',
    )
    not_csv_file_error_message = (By.ID, "notistack-snackbar")
    download_the_template_link = (
        By.CSS_SELECTOR,
        '[data-test-id="ManageLocations-defaultCSV"]',
    )
    review_button = (By.CSS_SELECTOR, '[data-test-id="snackbar-review-button"]')
    close_button = (By.CSS_SELECTOR, '[data-test-id="SettingsContent-closeButton"]')
    success_message = (By.CSS_SELECTOR, '[data-test-id="snackbar-title"]')
    view_details_button = (By.CSS_SELECTOR, '[data-test-id="viewDetailsButton"]')
    download_error_report = (By.CSS_SELECTOR, '[data-test-id="downloadErrorReport"]')

    def open_locations_page(self, url):
        """Method: open_locations_page"""
        try:
            test = inspect.stack()[0][3]
            expected_locations_url = f"{url}{self.path}"
            self.open(f"{expected_locations_url}")
            self.pause(0.5)
            actual_locations_url = self.get_current_url()
            assert (
                actual_locations_url == expected_locations_url
            ), f"Expected locations URL: {expected_locations_url}!"
            self.wait_for_element_present(self.name_header, 60)
            self.wait_for_element_visible(self.name_header, 60)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def upload_locations(self, file):
        """Method: upload_locations"""
        try:
            test = inspect.stack()[0][3]
            path = os.path.abspath(file)
            self.wait_for_element_present(self.name_header, 100)
            if self.is_element_present(locator=self.flag_on_locations_processed):
                print(self.is_element_present(locator=self.flag_on_locations_processed))
            else:
                print(self.is_element_present(locator=self.locations_processed))
            self.pause(4)
            if self.is_element_present(locator=self.delete_file_button):
                self.delete_all_locations()
            self.wait_for_element_present(self.upload_files_zone, 240)
            self.send_keys_to_element(self.upload_files_zone, path)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def verify_no_locations_uploaded(self):
        """Method verify_no_locations_uploaded"""
        if self.is_element_present(locator=self.delete_file_button):
            self.delete_all_locations()

    def locations_uploaded_should_be_correct_on_at_risk_table(
        self, number_of_locations
    ):
        """Method: locations_uploaded_should_be_correct_on_at_risk_table"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.analysis_bar_locations_total, 120)
            self.wait_for_element_visible(self.analysis_bar_locations_total, 120)
            locations_number1 = int(
                self.get_text_from_element(self.analysis_bar_locations_total).strip(
                    " total"
                )
            )
            assert locations_number1 == int(number_of_locations)
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def locations_processed_should_be_correct(self, number_of_locations):
        """Method: locations_processed_should_be_correct"""
        try:
            test = inspect.stack()[0][3]
            self.browser.switch_to.default_content()
            self.wait_for_element_present(self.name_header, 100)
            self.wait_for_element_present(self.delete_file_button, 100)
            if self.is_element_present(locator=self.locations_processed):
                locations_number = self.get_text_from_element(self.locations_processed)
            else:
                locations_number = self.get_text_from_element(
                    self.flag_on_locations_processed
                )
            assert locations_number == number_of_locations
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def delete_all_locations(self):
        """Method: delete_all_locations"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.delete_file_button, 120)
            self.wait_for_element_present(self.last_updated_time, 120)
            self.wait_for_element_visible(self.last_updated_time, 120)
            self.click_element(self.delete_file_button)
            if self.is_element_present(locator=self.delete_without_backup_button):
                self.click_element(self.delete_without_backup_button)
            else:
                self.wait_for_element_present(self.delete_file_confirmation_button, 120)
                self.click_element(self.delete_file_confirmation_button)
            self.wait_for_element_present(self.upload_files_zone, 120)
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def no_locations_should_be_uploaded(self):
        """Method: no_locations_should_be_uploaded"""
        try:
            test = inspect.stack()[0][3]
            assert self.is_element_present(locator=self.delete_file_button) is False
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def upload_message_should_be_visible(self):
        """Method: upload_message_should_be_visible"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.success_message, 120)
            self.wait_for_element_visible(self.success_message, 120)
            self.wait_for_element_present(self.review_button, 120)
            print(f"PASS: {test}")
            return True
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_review_button(self):
        """Method: click_review_button"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.review_button)
            self.pause(5)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def upload_error_message_should_be_visible(self):
        """Method: upload_error_message_should_be_visible"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.error_message_description, 120)
            self.wait_for_element_visible(self.error_message_description, 120)
            error = self.get_text_from_element(self.error_message_description)
            assert error in (
                "Click “Manage locations” to review the locations you tried to upload."
                "We had issues with at least one address. Please take a look."
            )
            print(f"PASS: {test}")
            return True
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def upload_not_csv_file_error_message_should_be_visible(self):
        """Method: upload_not_csv_file_error_message_should_be_visible"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.not_csv_file_error_message, 100)
            self.wait_for_element_visible(self.not_csv_file_error_message, 100)
            error = self.get_text_from_element(self.not_csv_file_error_message)
            assert (
                error
                == "This file isn’t in .CSV format. Please take a look and try again."
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def upload_big_csv_file_error_message_should_be_visible(self):
        """Method: upload_big_csv_file_error_message_should_be_visible"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.big_file_uploads_error_message, 100)
            self.wait_for_element_visible(self.big_file_uploads_error_message, 100)
            error = self.get_text_from_element(self.big_file_uploads_error_message)
            assert (
                error
                == "This file is too big, so we did not process any records. 4MB is the limit. Reduce the size and try again."
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def locations_hidden_should_equal(self, number_of_locations):
        """Method: locations_hidden_should_equal"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.name_header, 100)
            self.wait_for_element_present(self.delete_file_button, 100)
            if self.is_element_present(locator=self.locations_hidden_number):
                hidden_number = self.get_text_from_element(self.locations_hidden_number)
            else:
                hidden_number = self.get_text_from_element(
                    self.flag_on_locations_hidden_number
                )
            print(hidden_number)
            assert hidden_number == number_of_locations
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def upload_more_than_5000_locations_error_should_be_visible(self):
        """Method: upload_more_than_5000_locations"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.big_file_uploads_error_message, 100)
            self.wait_for_element_visible(self.big_file_uploads_error_message, 100)
            error = self.get_text_from_element(self.big_file_uploads_error_message)
            assert (
                error
                == "This file contains more than 5000 locations, so we can’t upload it. Edit the file to remove the extra locations, then try uploading, again."
            )
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def download_vulnerable_locations_file(self):
        """Method: download_vulnerable_locations_file"""
        try:
            test = inspect.stack()[0][3]
            self.generate_screenshot(test)
            self.send_key_element(self.Download_to_csv)
            self.pause(4)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed due to: {error}!")

    def upload_vulnerable_locations_file(self, downloaded_file):
        """Method: upload_vulnerable_locations_file"""
        try:
            test = inspect.stack()[0][3]
            self.upload_locations(downloaded_file)
            self.pause(4)
            error_title = self.get_text_from_element(self.snackbar_title)
            error_desc = self.get_text_from_element(self.snackbar_description)
            print(f"Error Title: {error_title}")
            print(f"Error Description: {error_desc}")
            assert error_title == "We couldn't process that file."
            assert error_desc == "Please check the file format and try again."
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed due to: {error}!")

    def download_locations_template(self):
        """Method: download_locations_template"""
        try:
            test = inspect.stack()[0][3]
            delete_button_exists = self.is_element_displayed(
                self.delete_file_button, 20
            )
            if delete_button_exists:
                self.delete_all_locations()
            self.generate_screenshot(test)
            self.click_element(self.download_the_template_link, 40)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed due to: {error}!")

    def upload_downloaded_template(self, downloaded_template_file):
        """Method: upload_downloaded_template"""
        try:
            test = inspect.stack()[0][3]
            self.upload_locations(downloaded_template_file)
            at_risk_location = self.get_text_from_element(self.at_risk_title)
            assert at_risk_location == "At-risk locations"
            assert (self.is_element_present(self.Download_to_csv)) is True
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def get_processed_location_count(self):
        """Method: get_processed_location_count"""
        try:
            test = inspect.stack()[0][3]
            processed_locations = self.get_text_from_element(self.processed_locations)
            print(f"PASS: {test}")
            return int(processed_locations)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def click_help_link(self):
        """Method: click_help_link"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.help_link)
            print(f"PASS: {test}")
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed due to: {error}!")

    def assert_downloaded_csv_locations_count_equals_processed_locations(
        self, downloaded_csv_locations
    ):
        """Method: assert_downloaded_csv_locations_count_equals_processed_locations"""
        try:
            test = inspect.stack()[0][3]
            rowcount = 0
            self.pause(5)
            # iterating through the whole file
            with open(downloaded_csv_locations, "r") as file_handle:
                for _ in file_handle:
                    rowcount += 1
            # delete one line because of the locations title
            assert self.get_processed_location_count() == rowcount - 1
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_view_details_button(self):
        """Method: click_view_details_button"""
        try:
            test = inspect.stack()[0][3]
            self.click_element(self.view_details_button)
            self.pause(5)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def click_download_error_report(self):
        """Method: click_download_error_report"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.download_error_report)
            self.click_element(self.download_error_report)
            self.pause(5)
            print(f"PASS: {test}")
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
