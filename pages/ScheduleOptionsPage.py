from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScheduleOptions:
    def __init__(self, driver):
        self.driver = driver

    #Locators. These may also vary on user preferences.

    open_ticket = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Elegir boleto abierto")')
    departure_tariff = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Elegir").instance(2)')
    return_tariff = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Elegir").instance(1)')

    def select_departure_tariff(self):
        departure_ticket = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.departure_tariff))
        departure_ticket.click()

    def select_return_tariff(self):
        return_ticket = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.return_tariff))
        return_ticket.click()

    def select_open_ticket(self):
        open_ticket = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.open_ticket))
        open_ticket.click()







