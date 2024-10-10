import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium_config import APPIUM_HOST, APPIUM_PORT
from Data.data import Data
from pages.DotersPage import DotersPage
from pages.HomePage import HomePage


class TestLogInDoters:

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

    def test_open_log_in_screen(self, appium_driver):
        home = HomePage(appium_driver)
        home.click_doters()
        doters = DotersPage(appium_driver)
        doters.click_log_in_button()


    def test_log_in(self, appium_driver):
        user_data = Data.get_user_data()
        doters = DotersPage(appium_driver)
        doters.write_user(
            email  = user_data["email"]
        )
        doters.write_user_password(
            password = user_data["password"]
        )

        doters.click_log_in_user()



