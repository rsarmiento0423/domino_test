""" DominoFinancialLossCalculator.py """
import inspect
from BaseFactory import *

# from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


class DominoFinancialLossCalculator(BaseFactory):
    """class: DominoFinancialLossCalculator"""

    path = "/#/"
    enter_annual_revenue_input_header = (
        By.CSS_SELECTOR,
        '[data-test-id="LocTypesAnnualRevenuesForm-title"]',
    )
    input1_annual_revenue = (
        By.CSS_SELECTOR,
        '[data-test-id="CurrencyInput0-annualRevenue"]',
    )
    input2_annual_revenue = (
        By.CSS_SELECTOR,
        '[data-test-id="CurrencyInput1-annualRevenue"]',
    )
    input3_annual_revenue = (
        By.CSS_SELECTOR,
        '[data-test-id="CurrencyInput2-annualRevenue"]',
    )
    analyze_button = (By.CSS_SELECTOR, '[data-test-id="SaveRevenues"]')
    reset_button = (By.CSS_SELECTOR, '[data-test-id="ResetRevenues"]')

    ### Dashboard
    dashboard_nav = (By.CSS_SELECTOR, '[data-test-id="MaterialityNav-dashboard"]')
    materiality_dashboard = (By.CSS_SELECTOR, '[data-test-id="MaterialityDashboard"]')
    materiality_drivers = (By.CSS_SELECTOR, '[data-test-id="Materiality:Drivers"]')
    materiality_metrics = (By.CSS_SELECTOR, '[data-test-id="MaterialityMetrics"]')

    mean_loss = (By.CSS_SELECTOR, '[data-test-id="MaterialityKPIs:meanLoss"]')
    revenue_percentage = (
        By.CSS_SELECTOR,
        '[data-test-id="MaterialityKPIs:revenuePercentage"]',
    )
    materiality_percentage = (
        By.CSS_SELECTOR,
        '[data-test-id="MaterialityKPIs:materialityPercentage"]',
    )
    over_materiality = (
        By.CSS_SELECTOR,
        '[data-test-id="MaterialityKPIs:overMateriality"]',
    )

    revenue_table = (By.CSS_SELECTOR, '[data-test-id="RevenueTable"]')
    location_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-locationAddress"]',
    )
    loss_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-loss"]',
    )
    downtime_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-downtime"]',
    )
    lifeline_table_header = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-lifeline"]',
    )
    first_table_location = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTable_go_to_location-0_locationAddress"]',
    )

    hazard_filter = (By.CSS_SELECTOR, '[data-test-id="HazardFilterButton"]')
    climate_toggle_switch = (By.CSS_SELECTOR, '[data-test-id="climate-toggle-switch"]')
    planning_horizon = (By.CSS_SELECTOR, '[data-test-id="picker-button-maintext"]')
    location_picker = (By.CSS_SELECTOR, '[data-test-id="locations-picker-button"]')
    export_financial_losses_button = (
        By.CSS_SELECTOR,
        '[data-test-id="export-financial-losses"]',
    )
    sort_by_location = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-locationAddress"]',
    )
    sort_by_loss = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-loss"]',
    )
    sort_by_downtime = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-downtime"]',
    )
    sort_by_lifeline = (
        By.CSS_SELECTOR,
        '[data-test-id="RevenueTableHeadCellSortable-lifeline"]',
    )
    rows_per_pages = (
        By.CSS_SELECTOR,
        '[class="MuiSelect-select MuiTablePagination-select MuiSelect-standard MuiInputBase-input css-s0y4gn"]',
    )
    close_financial_loss_calculator_button = (
        By.CSS_SELECTOR,
        '[data-test-id="MaterialityContent-closeButton"]',
    )

    ### Settings
    settings_nav = (By.CSS_SELECTOR, '[data-test-id="MaterialityNav-settings"]')
    settings_content = (By.CSS_SELECTOR, '[data-test-id="Materiality-content"]')
    financial_loss_threshold = (
        By.CSS_SELECTOR,
        '[data-test-id="PercentInput-MaterialityThreshold"]',
    )
    twelve_hours_link = (By.CSS_SELECTOR, '[data-test-id="Tab-0"]')
    one_day_link = (By.CSS_SELECTOR, '[data-test-id="Tab-1"]')
    seven_days_link = (By.CSS_SELECTOR, '[data-test-id="Tab-2"]')
    annual_revenue_link = (By.CSS_SELECTOR, '[data-test-id="Tab-3"]')
    additional_cost_link = (By.CSS_SELECTOR, '[data-test-id="Tab-4"]')
    input1_additional_cost = (
        By.CSS_SELECTOR,
        '[data-test-id="CurrencyInput0-additionalCost"]',
    )
    input2_additional_cost = (
        By.CSS_SELECTOR,
        '[data-test-id="CurrencyInput1-additionalCost"]',
    )
    input3_additional_cost = (
        By.CSS_SELECTOR,
        '[data-test-id="CurrencyInput2-additionalCost"]',
    )
    save_changes_button = (By.CSS_SELECTOR, '[data-test-id="SaveEditing"]')
    cancel_button = (By.CSS_SELECTOR, '[data-test-id="CancelEditing"]')
    financial_loss_calculator_help2 = (By.PARTIAL_LINK_TEXT, "About financial")
    location_column_data = (By.CSS_SELECTOR, "table > tbody > tr > td:nth-child(1)")
    loss_column_data = (By.CSS_SELECTOR, "table > tbody > tr > td:nth-child(2)")
    downtime_column_data = (By.CSS_SELECTOR, "table > tbody > tr > td:nth-child(3)")
    lifeline_column_data = (By.CSS_SELECTOR, "table > tbody > tr > td:nth-child(4)")
    right_arrow_button = (By.CSS_SELECTOR, '[data-testid="KeyboardArrowRightIcon"]')
    left_arrow_button = (By.CSS_SELECTOR, '[data-testid="KeyboardArrowLeftIcon"]')
    locations_dropdown_list = (
        By.CSS_SELECTOR,
        'button[name="locations-button"] [data-testid="ExpandMoreIcon"]',
    )
    select_rite_aid = (By.CSS_SELECTOR, '[data-test-id="menuitem-Rite Aid"]')
    apply_locations_button = (
        By.CSS_SELECTOR,
        'div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation0.MuiPopover-paper.css-w1f3wu > form > footer > div > button[name="apply"]',
    )
    restore_defaults_locations_button = (
        By.CSS_SELECTOR,
        "div.MuiPopover-root.MuiModal-root.css-jp7szo > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation0.MuiPopover-paper.css-w1f3wu > form > footer > button",
    )
    cancel_locations_button = (By.CSS_SELECTOR, 'button[name="cancel"]')

    def assert_annual_revenue_input(self):
        """Method: assert_annual_revenue_input"""
        try:
            test = inspect.stack()[0][3]
            actual_enter_annual_revenue_header = self.get_text_from_element(
                self.enter_annual_revenue_input_header
            )
            assert (
                actual_enter_annual_revenue_header
                == "To get started, enter your annual revenue for each property type."
            ), "Wrong header displayed for entering annual revenue!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def enter_annual_revenue_data(self, input1, input2, input3, bInitial=True):
        """Method: enter_annual_revenue_data"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.input1_annual_revenue, 60)
            self.clear_element_text(self.input1_annual_revenue)
            self.clear_element_text(self.input2_annual_revenue)
            self.clear_element_text(self.input3_annual_revenue)
            self.send_keys_to_element(self.input1_annual_revenue, input1)
            self.send_keys_to_element(self.input2_annual_revenue, input2)
            self.send_keys_to_element(self.input3_annual_revenue, input3)
            if bInitial:
                self.wait_for_element_present(self.analyze_button, 60)
                self.click_element(self.analyze_button, 60)
            else:
                self.wait_for_element_present(self.save_changes_button)
                self.click_element(self.save_changes_button)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def reset_annual_revenue_data(self, input1, input2, input3):
        """Method: reset_annual_revenue_data"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.input1_annual_revenue, 60)
            self.send_keys_to_element(self.input1_annual_revenue, input1)
            self.send_keys_to_element(self.input2_annual_revenue, input2)
            self.send_keys_to_element(self.input3_annual_revenue, input3)
            self.wait_for_element_present(self.reset_button, 60)
            self.click_element(self.reset_button, 60)
            assert (
                len(self.get_attribute_value(self.input1_annual_revenue)) == 0
            ), "Input1 was not cleared after reset!"
            assert (
                len(self.get_attribute_value(self.input2_annual_revenue)) == 0
            ), "Input2 was not cleared after reset!"
            assert (
                len(self.get_attribute_value(self.input3_annual_revenue)) == 0
            ), "Input3 was not cleared after reset!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_dashboard_revenue_with_financial_loss_drivers(self):
        """Method: assert_dashboard_revenue_with_financial_loss_drivers"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.materiality_dashboard, 60)
            assert self.is_element_displayed(
                self.materiality_drivers,
            ), "Missing materiality drivers!"
            assert self.is_element_displayed(
                self.materiality_metrics
            ), "Missing materiality metrics!"
            assert self.is_element_displayed(
                self.revenue_table, "Missing revenue table"
            )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_export_button(self):
        """Method: click_export_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.export_financial_losses_button, 60)
            self.click_element(self.export_financial_losses_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_settings_nav(self):
        """Method: click_settings_nav"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.settings_nav, 60)
            self.click_element(self.settings_nav, 60)
            assert self.is_element_displayed(
                self.settings_content
            ), "Missing Settings content!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def enter_materiality_threshold(self, threshold):
        """Method: enter_materiality_threshold"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.financial_loss_threshold, 60)
            self.send_keys_to_element(self.financial_loss_threshold, threshold)
            self.send_key_element(self.financial_loss_threshold)
            actual_value = self.get_attribute_value(self.financial_loss_threshold)
            assert threshold == actual_value, "Wrong materiality threshold entered!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_additional_cost(self):
        """Method: click_additional_cost"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.additional_cost_link, 60)
            self.click_element(self.additional_cost_link, 60)
            assert self.is_element_displayed(
                self.settings_content
            ), "Missing Settings content!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_annual_revenue(self):
        """Method: click_annual_revenue"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.annual_revenue_link, 60)
            self.click_element(self.annual_revenue_link, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def enter_additional_cost_data(self, input1, input2, input3):
        """Method: enter_additional_cost_data"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.input1_additional_cost, 60)
            self.clear_element_text(self.input1_additional_cost)
            self.clear_element_text(self.input2_additional_cost)
            self.clear_element_text(self.input3_additional_cost)
            self.send_keys_to_element(self.input1_additional_cost, input1)
            self.send_keys_to_element(self.input2_additional_cost, input2)
            self.send_keys_to_element(self.input3_additional_cost, input3)
            self.wait_for_element_present(self.save_changes_button, 60)
            self.click_element(self.save_changes_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_close_flc_button(self):
        """Method: click_close_flc_button"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(
                self.close_financial_loss_calculator_button, 60
            )
            self.click_element(self.close_financial_loss_calculator_button, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_dashboard_flc_help_link(self):
        """Method: click_dashboard_flc_help_link"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.financial_loss_calculator_help2, 60)
            self.click_element(self.financial_loss_calculator_help2, 60)
            lst_win_handles = self.browser.window_handles
            assert (
                len(lst_win_handles) > 1
            ), "Financial Loss Calculate Help not opened after clicking 'about Financial Loss calculator'!"
            for win_handle in lst_win_handles:
                self.browser.switch_to.window(win_handle)
            actual_url = self.get_current_url()
            print(f"Got Financial Loss Calculator URL: {actual_url}")
            assert (
                "articles/6950409-financial-loss-calculator" in actual_url
            ), "Wrong Financial Loss URL found!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_dashboard_table_and_controls(self):
        """Method: assert_dashboard_table_and_controls"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.materiality_dashboard, 60)
            assert self.is_element_displayed(self.mean_loss, "Missing mean loss!")
            assert self.is_element_displayed(
                self.revenue_percentage, "Missing revenue percentage!"
            )
            assert self.is_element_displayed(
                self.materiality_percentage, "Missing materiality percentage!"
            )
            assert self.is_element_displayed(
                self.over_materiality, "Missing over materiality!"
            )

            assert self.is_element_displayed(
                self.hazard_filter, "Missing hazard filter!"
            )
            assert self.is_element_displayed(
                self.climate_toggle_switch, "Missing climate toggle switch!"
            )
            assert self.is_element_displayed(
                self.planning_horizon, "Missing planning horizon!"
            )
            assert self.is_element_displayed(
                self.location_picker, "Missing location picker!"
            )

            assert self.is_element_displayed(
                self.revenue_table, "Missing revenue table!"
            )
            assert self.is_element_displayed(
                self.location_table_header, "Missing location table header!"
            )
            assert self.is_element_displayed(
                self.loss_table_header, "Missing loss table header!"
            )
            assert self.is_element_displayed(
                self.downtime_table_header, "Missing downtime table header!"
            )
            assert self.is_element_displayed(
                self.lifeline_table_header, "Missing lifeline table header!"
            )
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_first_location_dashboard(self):
        """Method: click_first_location_dashboard"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.first_table_location, 60)
            self.click_element(self.first_table_location, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def sort_loss_column(self):
        """Method: sort_loss_column"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.sort_by_loss, 60)
            self.click_element(self.sort_by_loss, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def sort_location_column(self):
        """Method: sort_location_column"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.sort_by_location, 60)
            self.click_element(self.sort_by_location, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def sort_downtime_column(self):
        """Method: sort_downtime_column"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.sort_by_downtime, 60)
            self.click_element(self.sort_by_downtime, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def sort_lifeline_column(self):
        """Method: sort_lifeline_column"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.sort_by_lifeline, 60)
            self.click_element(self.sort_by_lifeline, 60)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def check_rows_per_page(self):
        """Method: check_rows_per_page"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.rows_per_pages, 60)
            assert self.is_element_displayed(
                self.rows_per_pages, "Missing rows per page!"
            )
            self.wait_for_element_present(self.right_arrow_button, 60)
            self.click_element(self.right_arrow_button)
            self.wait_for_element_present(self.left_arrow_button, 60)
            self.click_element(self.left_arrow_button)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def assert_column_data(self, colname, order="dsc"):
        """Method: assert_column_data"""
        try:
            test = inspect.stack()[0][3]
            lstvalues = []
            if colname == "loss":
                elements = self.browser.find_elements(*self.loss_column_data)
            elif colname == "location":
                elements = self.browser.find_elements(*self.location_column_data)
            elif colname == "downtime":
                elements = self.browser.find_elements(*self.downtime_column_data)
            elif colname == "lifeline":
                elements = self.browser.find_elements(*self.lifeline_column_data)
            else:
                print(f"Skipping verifying sort order for column name: {colname}")
                return
            print(f"Total {colname} found on page: {len(elements)}")
            for data in elements:
                print(data.text)
                lstvalues.append(data.text)
            top_val = lstvalues[0]
            bot_val = lstvalues[-1]
            if colname == "downtime":
                top_val = self.extract_num(top_val)
                bot_val = self.extract_num(bot_val)
            if order == "dsc":
                assert top_val >= bot_val, f"{colname} not sorted in descending order!"
            else:
                assert top_val <= bot_val, f"{colname} not sorted in ascending order!"
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to: {error}!")

    def click_locations(self):
        """Method: click_locations"""
        try:
            test = inspect.stack()[0][3]
            self.wait_for_element_present(self.locations_dropdown_list, 60)
            self.click_element(self.locations_dropdown_list)

            self.wait_for_element_present(self.select_rite_aid, 60)
            self.click_element(self.select_rite_aid)

            self.wait_for_element_present(self.apply_locations_button, 60)
            self.click_element(self.apply_locations_button)

            self.wait_for_element_present(self.locations_dropdown_list, 60)
            self.click_element(self.locations_dropdown_list)

            self.wait_for_element_present(self.restore_defaults_locations_button, 60)
            self.send_key_element(self.restore_defaults_locations_button)
            self.click_element(self.apply_locations_button)
            print(f"PASS: {test}")
        except Exception as error:
            self.generate_screenshot(test)
            raise Exception(f"Failed {test} due to {error}!")
