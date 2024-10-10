import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium_config import APPIUM_HOST, APPIUM_PORT
from Data.data import Data
from Utils.helpers import MobileHelpers
from pages.HomePage import HomePage
from pages.ScheduleOptionsPage import ScheduleOptions
from pages.SeatsPage import SeatsPage
from pages.PassengersDataPage import PassengerData
from pages.PaymentPage import PaymentPage


class LogInDoters:

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


