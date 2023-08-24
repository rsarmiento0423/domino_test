""" DominoIntercomMessagePage.py """
import inspect
from BaseFactory import *
from selenium.webdriver.common.by import By


class DominoIntercomMessagePage(BaseFactory):
    """class: DominoIntercomMessagePage"""

    intercom_button = (By.CSS_SELECTOR, '[data-test-id="IntercomButton"]')
    login_frame = (By.ID, "login-iframe")
    intercom_iframe = (By.NAME, "intercom-messenger-frame")
    Intercom_screen = (By.CSS_SELECTOR, '[data-testid="spaces-home"]')
    messages_button = (By.CSS_SELECTOR, '[data-testid="messages"]')
    cancel_button = (By.CSS_SELECTOR, '[aria-label="Close"]')
    new_conversation_button = (By.CSS_SELECTOR, "div.intercom-home-screen strong")
    search_articles = (By.CSS_SELECTOR, "input.search__input")
    search_for_help_button = (By.CSS_SELECTOR, "div.intercom-home-screen button")
    search_for_help_input = (By.CSS_SELECTOR, 'input[aria-label="Search for help"]')
    search_help_text = (By.CSS_SELECTOR, "div.intercom-home-screen button span")
    search_result = (By.CSS_SELECTOR, "li div p span")
    help_header = (By.CSS_SELECTOR, "section > h1")
    help_id = (By.CSS_SELECTOR, '[data-testid="help"]')
    home_icon = (By.CSS_SELECTOR, '[data-testid="home"]')
    intercom_message = (By.CSS_SELECTOR, "div.intercom-home-screen h2")
    intercom_hi_user = (By.CSS_SELECTOR, "div.intercom-home-screen h1")
    back_button = (By.CSS_SELECTOR, '[data-testid="go-back"]')
    message_textbox = (By.NAME, "message")
    send_message_button = (By.CSS_SELECTOR, '[data-testid="send-a-message-button"]')
    intercom_comment = (By.CSS_SELECTOR, "div.intercom-block-paragraph")
    composer_send_button = (By.CSS_SELECTOR, "button.intercom-composer-send-button")
    locale_link = (By.ID, "kc-current-locale-link")
    language_link = (By.CSS_SELECTOR, "ul li a")
    start_message = (
        By.CSS_SELECTOR,
        "div.intercom-home-screen-start-conversation-card-new >div > h2.intercom-messenger-card-text",
    )

    def assert_intercom_icon_is_displayed(self):
        """Method: assert_intercom_icon_is_displayed"""
        self.wait_for_element_visible(self.intercom_button, 30)

    def click_intercom_icon(self):
        """Method: click_intercom_icon"""
        self.click_element(self.intercom_button, 20)

    def assert_intercom_screen_is_opened(self):
        """Method: assert_intercom_message_is_opened"""
        self.switch_to_iframe(self.intercom_iframe)

    def assert_intercom_screen_content(self, first_name):
        """Method: assert_intercom_message_content"""
        test = inspect.stack()[0][3]
        try:
            self.click_element(self.cancel_button, 30)
            self.click_element(self.intercom_button, 30)
            self.switch_to_iframe(self.intercom_iframe)
            self.click_element(self.help_id)
            self.click_element(self.messages_button)
            self.click_element(self.home_icon)
            user_message = self.get_text_from_element(self.intercom_message, 30)
            user_name = self.get_text_from_element(self.intercom_hi_user)
            print(user_message)
            print(user_name)
            assert user_message == "How can we help?"
            assert user_name == f"Hi {first_name}!"

        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def assert_help_page_content(self):
        """Method: assert_new_tab"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.search_articles)
            help_header = self.get_text_from_element(self.help_header)
            assert help_header == "Advice and answers from the One Concern Team"
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def send_intercom_message(self, message):
        """Method: send_intercom_message"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.messages_button)
            self.click_element(self.messages_button)
            self.click_element(self.send_message_button)
            self.wait_for_element_visible(self.message_textbox)
            self.click_element(self.message_textbox)
            self.send_keys_to_element(self.message_textbox, message)
            self.click_element(self.composer_send_button)
            sent_message = self.get_text_from_element(self.intercom_comment)
            assert sent_message == message
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def search_for_articles(self, article):
        """Method: search_for_articles"""
        test = inspect.stack()[0][3]
        try:

            self.click_element(self.search_for_help_button)
            assert self.is_element_present(self.search_for_help_input) is True
            self.send_keys_to_element(self.search_for_help_input, article)
        except RuntimeError as error:
            self.generate_screenshot(test)
            raise RuntimeError(f"Failed {test} due to: {error}!")

    def assert_search_results(self):
        """Method: assert_search_results"""
        test = inspect.stack()[0][3]
        try:
            result = self.get_number_of_elements(self.search_result)
            # assert search result is more than 1 article
            assert len(result) > 1
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")

    def switch_language(self):
        """Method: switch_language"""
        self.wait_for_element_present(self.login_frame, 30)
        self.switch_to_iframe(self.login_frame)
        self.click_element(self.locale_link)
        self.click_element(self.language_link)
        self.browser.switch_to.default_content()

    def assert_japan_items(self):
        """Method: assert_japan_items"""
        test = inspect.stack()[0][3]
        try:
            self.wait_for_element_visible(self.intercom_hi_user)
            self.pause(2)
            welcome = self.get_text_from_element(self.intercom_hi_user)
            assert welcome == "お問い合わせ窓口"
            search_for_help = self.get_text_from_element(self.search_help_text)
            assert search_for_help == "ヘルプの検索"
        except AssertionError as error:
            self.generate_screenshot(test)
            raise AssertionError(f"Failed {test} due to: {error}!")
