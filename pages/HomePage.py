from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver


    origin_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecciona tu Origen")')

    destination_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecciona tu Destino")')

    departure_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Fecha de Salida")')

    right_arrow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')

    left_arrow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')

    return_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("(Opcional)")')

    search_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUSCAR")')

    #These Locators may vary depending on user expectations:
    origin_city = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aguascalientes, AGUASCALIENTES")')

    destination_city = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Guadalajara, GUADALAJARA")')

    departure_date = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("30")')

    return_date = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("7")')

    #Methods

    def click_origin_field(self):
        self.driver.find_element(*self.origin_field).click()

    def click_destination_field(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.destination_field))
        origin_element.click()


    def click_departure_calendar(self):
        self.driver.find_element(*self.departure_field).click()

    def click_return_calendar(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.return_field))
        origin_element.click()


    def click_search_button(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.search_button))
        origin_element.click()


    def set_origin(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.origin_city))
        origin_element.click()

    def set_destination(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.destination_city))
        origin_element.click()

    def set_depart_calendar(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.departure_date))
        origin_element.click()

    def click_right_arrow(self):
        self.driver.find_element(*self.right_arrow).click()

    def set_return_calendar(self):
        origin_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.return_date))
        origin_element.click()


    #Steps

    def set_departure(self):
        self.click_origin_field()
        self.set_origin()

    def set_return(self):
        self.click_destination_field()
        self.set_destination()

    def set_departure_date(self):
        self.click_departure_calendar()
        self.set_depart_calendar()

    def set_return_date(self):
        self.click_return_calendar()
        self.click_right_arrow()
        self.set_return_calendar()

    def search_round_trip(self):
        self.set_departure()
        self.set_return()
        self.set_departure_date()
        self.set_return_date()
        self.click_search_button()
