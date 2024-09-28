from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators:
    use_passenger_data_radial = (AppiumBy.ANDROID_UIAUTOMATOR, 'android.widget.Switch')

    name_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nombre (s)*")')
    last_name_one_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Primer apellido*")')
    last_name_two_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Segundo apellido")')
    phone_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Teléfono celular *")')

    card_name_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("holderName")')
    card_number_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("cardNumber")')

    month_list = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mes")')

    #Dynamic Locator:
    expiration_month = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{month}")')

    year_list = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Año")')

    #Dynamic Locator:
    expiration_year = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{year}")')

    cvv_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("cvv2")')

    trip_details= (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Detalles de tu viaje")')
    close_details_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')

    submit_payment_button = (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Pagar')]")

    #Methods

    def use_first_passenger_data(self):
        self.driver.find_element(*self.use_passenger_data_radial).click()

    def write_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def write_last_name_one(self, last_name_one):
        self.driver.find_element(*self.last_name_one_field).send_keys(last_name_one)

    def write_last_name_two(self, last_name_two):
        self.driver.find_element(*self.last_name_two_field).send_keys(last_name_two)

    def write_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def write_card_name(self, card_name):
        self.driver.find_element(*self.card_name_field).send_keys(card_name)


    def write_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def select_expiration_month(self, month):
        self.driver.find_element(*self.month_list).click()
        month_dynamic = (AppiumBy.ANDROID_UIAUTOMATOR, self.expiration_month[1].format(month=month))
        self.driver.find_element(*month_dynamic).click()

    def select_expiration_year(self, year):
        self.driver.find_element(*self.year_list).click()
        year_dynamic = (AppiumBy.ANDROID_UIAUTOMATOR, self.expiration_year[1].format(year=year))
        self.driver.find_element(*year_dynamic).click()

    def write_cvv(self, cvv):
        self.driver.find_element(*self.cvv_field).send_keys(cvv)

    def click_trip_details(self):
        self.driver.find_element(*self.trip_details).click()

    def close_trip_details(self):
        self.driver.find_element(*self.close_details_button).click()

    def submit_payment(self):
        origin_element = WebDriverWait(self.driver, 3 ).until(
        EC.visibility_of_element_located(self.submit_payment_button))
        origin_element.click()

    #Steps:

    def fill_passenger_data(self, name, last_name_one, last_name_two, phone):
        self.write_name(name)
        self.write_last_name_one(last_name_one)
        self.write_last_name_two(last_name_two)
        self.write_phone(phone)


    def fill_card_data(self, card_name, card_number, expiration_month, expiration_year, cvv):
        self.write_card_name(card_name)
        self.write_card_number(card_number)
        self.select_expiration_month(expiration_month)
        self.select_expiration_year(expiration_year)
        self.write_cvv(cvv)

    def check_trip_details(self):
        self.click_trip_details()
        time.sleep(4)
        self.close_trip_details()






