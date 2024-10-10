from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeatsPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators:

    departure_seat = (AppiumBy.XPATH, '//android.widget.TextView("[departure_seat]")')
    seat_seven = (AppiumBy.XPATH, '//android.widget.TextView[@text="3"]')

    continue_button = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Continuar con")]')

    @staticmethod
    def generate_seat_locator(seat):
        return  (AppiumBy.XPATH, f'//android.widget.TextView[@text="{seat}"]')

    #Methods

    def select_departure_seat(self, departure_seat):
        seat =  self.generate_seat_locator(departure_seat)
        WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(seat)).click()


    def select_return_seat(self, return_seat):
        seat = self.generate_seat_locator(return_seat)
        WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(seat)).click()





