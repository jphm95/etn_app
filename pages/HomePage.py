from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver,):
        self.driver = driver

    doters_element = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Doters")')

    origin_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecciona tu Origen")')

    destination_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecciona tu Destino")')

    departure_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Fecha de Salida")')

    right_arrow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')

    left_arrow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')

    return_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("(Opcional)")')

    search_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUSCAR")')

    #These locators were designed dynamically to accommodate user expectations and input flexibility.

    month_locator = (AppiumBy.XPATH, '//android.widget.SeekBar[contains(@content-desc, "Dom, Lun, Mar, Mie, Jue, Vie, Sáb")]')

    depart_day = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("[departure_day]")')

    return_day = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("[return_day]")')


    #Functions for dynamic locators:
    @staticmethod
    def generate_city_locator(city_name):
        return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{city_name}, {city_name.upper()}")'

    @staticmethod
    def generate_day_locator(day):
        return AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{day}")'

    # Methods:
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


    def set_origin(self, origin_city):
        origin_locator = self.generate_city_locator(origin_city)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(origin_locator)).click()


    def set_destination(self, destination_city):
        destination_locator = self.generate_city_locator(destination_city)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(destination_locator)).click()



    def click_right_arrow(self):
        self.driver.find_element(*self.right_arrow).click()

    def select_depart_month(self, depart_month):
     #   current_month = self.driver.find_element(*self.month_locator)
        wait = WebDriverWait(self.driver, 5)
        current_month = wait.until(EC.visibility_of_element_located(self.month_locator)
                                   )
        month_text = current_month.get_attribute('content-desc')
        current_month = month_text.split(' ')[0]

        while current_month != depart_month:
            self.click_right_arrow()

            current_month = self.driver.find_element(*self.month_locator)
            month_text = current_month.get_attribute('content-desc')
            current_month = month_text.split(' ')[0]

    def select_return_month(self, return_month):
        current_month = self.driver.find_element(*self.month_locator)
        wait = WebDriverWait(self.driver, 5)
        current_month = wait.until(EC.visibility_of_element_located(self.month_locator)
      )
        month_text = current_month.get_attribute('content-desc')
        current_month = month_text.split(' ')[0]

        while current_month != return_month:
            self.click_right_arrow()

            current_month = self.driver.find_element(*self.month_locator)
            month_text = current_month.get_attribute('content-desc')
            current_month = month_text.split(' ')[0]

    def set_depart_day(self, depart_day):
        depart_locator = self.generate_day_locator(depart_day)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(depart_locator)).click()


    def set_return_day(self, return_day):
        return_locator = self.generate_day_locator(return_day)
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(return_locator)).click()

    def click_doters(self):
        self.driver.find_element(*self.doters_element).click()


    #Steps

    def set_origin_city(self, origin_city):
        self.click_origin_field()
        self.set_origin(origin_city)

    def set_destination_city(self, destination_city):
        self.click_destination_field()
        self.set_destination(destination_city)

    def set_departure_date(self, depart_month, depart_day):
        self.click_departure_calendar()
        self.select_depart_month(depart_month)
        self.set_depart_day(depart_day)

    def set_return_date(self, return_month, return_day,):
        self.click_return_calendar()
        self.select_return_month(return_month)
        self.set_return_day(return_day)

    def search_round_trip(self, origin_city, destination_city, depart_month,  depart_day, return_month, return_day):
        self.set_origin_city(origin_city)
        self.set_destination_city(destination_city)
        self.set_departure_date(depart_month, depart_day)
        self.set_return_date(return_month, return_day)


    def search_single_trip(self, origin_city, destination_city, depart_month, depart_day):
        self.set_origin_city(origin_city)
        self.set_destination_city(destination_city)
        self.set_departure_date(depart_month, depart_day)



