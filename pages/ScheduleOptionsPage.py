from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScheduleOptions:
    def __init__(self, driver):
        self.driver = driver

    #Locators. These may also vary on user preferences.

    departure_tariff = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Elegir").instance(2)')
    return_tariff = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Elegir").instance(1)')

    def select_departure_tariff(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.departure_tariff))
        origin_element.click()

    def select_return_tariff(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.return_tariff))
        origin_element.click()




