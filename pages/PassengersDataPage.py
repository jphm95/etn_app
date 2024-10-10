from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.helpers import MobileHelpers

class PassengerData:
    def __init__(self, driver):
        self.driver = driver

    #Locators

    name_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nombre (s)*")')
    last_name_one = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Primer apellido*")')
    last_name_two = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Segundo apellido")')
    email_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Correo Electrónico * (Obligatorio)")')

    category_spinner = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Spinner")')

    adult_tariff = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adulto")')
    insen_tariff = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("INSEN")')
    pcc_tariff =  (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Persona con Discapacidad")')

    depart_insurance_radial = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Switch").instance(0)')
    return_insurance_radial = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Switch").instance(1)')

    next_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Siguiente")')

    #Methods

    def write_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def write_last_name_one(self, last_name_one):
        self.driver.find_element(*self.last_name_one).send_keys(last_name_one)

    def write_last_name_two(self, last_name_two):
        self.driver.find_element(*self.last_name_two).send_keys(last_name_two)

    def write_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def open_category_spinner(self):
        self.driver.find_element(*self.category_spinner).click()

    def click_adult_tariff(self):
        self.driver.find_element(*self.adult_tariff).click()

    def click_insen_tariff(self):
        self.driver.find_element(*self.insen_tariff).click()

    def click_pcd_tariff(self):
        self.driver.find_element(*self.pcc_tariff).click()

    def accept_depart_insurance(self):
        self.driver.find_element(*self.depart_insurance_radial).click()

    def accept_return_insurance(self):
        self.driver.find_element(*self.return_insurance_radial).click()

    def go_next_screen(self):
        self.driver.find_element(*self.next_button).click()





    #Setps:

    def fill_passenger_data(self, name, last_name_one, last_name_two, email):
        self.write_name(name)
        self.write_last_name_one(last_name_one)
        self.write_last_name_two(last_name_two)
        self.write_email(email)


    def select_insen_tariff(self):
        self.open_category_spinner()
        self.click_insen_tariff()

    def select_pcc_tariff(self):
         self.open_category_spinner()
         self.click_pcd_tariff()

    def accept_insurances(self):
        self.accept_depart_insurance()
        self.accept_return_insurance()

    

