from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.helpers import MobileHelpers

class ScheduleOptions:
    def __init__(self, driver):
        self.driver = driver
        self.mobile_helpers = MobileHelpers(driver)

    """
    Since schedule options can vary, these methods provide flexibility, especially given that locators might be unstable.
    This is due to the different schedules and varying numbers of options for each destination.
    """

    def select_departure_tariff(self, target_time):
        departure_ticket = self.mobile_helpers.scroll_to_partial_text(target_time)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of(departure_ticket))
        departure_ticket.click()

    def select_return_tariff(self, target_time):
        return_ticket = self.mobile_helpers.scroll_to_partial_text(target_time)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of(return_ticket))
        return_ticket.click()








