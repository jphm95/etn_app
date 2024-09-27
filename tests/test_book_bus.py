import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from Data.data import Data
from Utils.helpers import MobileHelpers
from appium_config import APPIUM_HOST, APPIUM_PORT
from pages.HomePage import HomePage
from pages.PassengersDataPage import PassengerData
from pages.PaymentPage import PaymentPage
from pages.ScheduleOptionsPage import ScheduleOptions
from pages.SeatsPage import SeatsPage


class TestBookBus:
    @pytest.fixture(scope='function')
    def appium_driver(self, appium_service):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platform_version = '15.0'
        options.device_name = 'Pixel 8a API 35'
        options.automation_name = 'Uiautomator2'
        options.app_package =  'mx.com.etn.etnturistarlujo'
        options.app_activity = 'com.gfa.primeraplus.MainActivity'
        options.no_reset = True

        driver = webdriver.Remote(
            command_executor=f'http://{APPIUM_HOST}:{APPIUM_PORT}',
            options=options)

        yield driver
        driver.quit()


    def test_search_buses(self, appium_driver):
        home_page = HomePage(appium_driver)
        home_page.search_round_trip()

    def test_select_departure(self, appium_driver):
        schedule_page = ScheduleOptions(appium_driver)
        schedule_page.select_departure_tariff()

    def test_select_return(self, appium_driver):
        schedule_page = ScheduleOptions(appium_driver)
        schedule_page.select_return_tariff()

    def test_select_seats(self, appium_driver):
        seats_page = SeatsPage(appium_driver)
        seats_page.select_seat_one()
        seats_page.select_seat_seven()

    def test_fill_passenger_data(self, appium_driver):
        passenger_info = Data.get_passenger_data()
        passenger_data = PassengerData(appium_driver)
        passenger_data.fill_passenger_data(
            name = passenger_info["name"],
            last_name_one = passenger_info["last_name_one"],
            last_name_two = passenger_info["last_name_two"],
            email = passenger_info["email"]
        )
        helper = MobileHelpers(appium_driver)
        helper.scroll_to_text("Siguiente")


    def test_accept_insurance(self, appium_driver):
        passenger_data = PassengerData(appium_driver)
        passenger_data.accept_insurances()

    def test_submit_passenger_data(self, appium_driver):
        passenger_data = PassengerData(appium_driver)
        passenger_data.go_next_screen()

    def test_submit_card_holder_data(self, appium_driver):
        payment_data = Data.get_passenger_data()
        payment_screen = PaymentPage(appium_driver)
        payment_screen.fill_passenger_data(
        name = payment_data["name"],
        last_name_one = payment_data["last_name_one"],
        last_name_two = payment_data["last_name_two"],
        phone = payment_data["phone"]
        )
        helper = MobileHelpers(appium_driver)
        helper.scroll_to_text("Resumen del viaje")


    def test_submit_card_data(self, appium_driver):
        payment_data = Data.get_payment_data()
        payment_screen = PaymentPage(appium_driver)
        payment_screen.fill_card_data(
        card_name = payment_data["card_name"],
        card_number = payment_data["card_number"],
        expiration_month = payment_data["expiration_month"],
        expiration_year = payment_data["expiration_year"],
        cvv = payment_data["cvv"]
        )
        helper = MobileHelpers
        helper.scroll_to_partial_text("Pagar")

    def test_submit_payment(self, appium_driver):
        payment_screen = PaymentPage(appium_driver)
        payment_screen.check_trip_details()
        payment_screen.submit_payment()
        















