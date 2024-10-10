import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium_config import APPIUM_HOST, APPIUM_PORT
from Data.data import Data
from Utils.helpers import MobileHelpers
from pages.DotersPage import DotersPage
from pages.HomePage import HomePage


class TestSingUpDoters:

    @pytest.fixture(scope='function')
    def appium_driver(self, appium_service):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platform_version = '15.0'
        options.device_name = 'Pixel 8a API 35'
        options.automation_name = 'Uiautomator2'
        options.app_package = 'mx.com.etn.etnturistarlujo'
        options.app_activity = 'com.gfa.primeraplus.MainActivity'
        options.no_reset = True

        driver = webdriver.Remote(
            command_executor=f'http://{APPIUM_HOST}:{APPIUM_PORT}',
            options=options)

        yield driver
        driver.quit()

    def test_open_sing_up_form(self, appium_driver):
        home = HomePage(appium_driver)
        home.click_doters()
        doters = DotersPage(appium_driver)
        doters.click_sign_in_button()


    def test_fill_personal_form(self, appium_driver):
        personal_data = Data.get_passenger_data()
        doters = DotersPage(appium_driver)
        doters.fill_personal_data(
            name = personal_data["name"],
            last_name_one = personal_data["last_name_one"],
            last_name_two = personal_data["last_name_two"],
            birthday = personal_data["birthday"]
        )

    def test_fill_contact_data(self, appium_driver):
        personal_data = Data.get_passenger_data()
        doters = DotersPage(appium_driver)
        doters.fill_contact_data(
            email = personal_data["email"],
            phone = personal_data["phone"]
        )
        helper = MobileHelpers(appium_driver)
        helper.scroll_to_text("Confirma contraseña")


    def test_set_password(self, appium_driver):
        personal_data = Data.get_user_data()
        doters = DotersPage(appium_driver)
        doters.set_password(
            password = personal_data["password"],
        )



    def test_submit_form(self, appium_driver):
        doters = DotersPage(appium_driver)
        doters.accept_terms()
        doters.click_create_account_button()







