from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DotersPage:
    def __init__(self, driver):
        self.driver = driver

    sign_up_button = (AppiumBy.ANDROID_UIAUTOMATOR, '')
    log_in_button = (AppiumBy.ANDROID_UIAUTOMATOR, '')


    #Sign Up Screen Locators:

    name_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("name")')
    last_name_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("lastname")')
    birthday_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(3)')
    email_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(4)')
    phone_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("phone")' )
    country_code = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Spinner")')
    password_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("password")')
    confirm_password_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("password2")')
    check_box_terms = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("customCheck1")')
    create_account_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Crear cuenta")')

    #Log In Screen Locators:

    user_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("userInput")')
    password_user = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
    log_in_user_button =(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')

    #Methods:
    #Create account
    def click_sign_in_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(*self.sign_up_button)).click()

    def click_log_in_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(*self.log_in_button)).click()

    def write_name(self, name):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(*self.name_field)).send_keys(name)


    def write_full_last_name(self, last_name_one, last_name_two):
        self.driver.find_element(*self.last_name_field).send_keys(last_name_one, last_name_two)

    def write_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def write_day_of_birth(self, birthday):
        self.driver.find_element(*self.birthday_field).send_keys(birthday)

    def write_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def write_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def confirm_password(self, password):
        self.driver.find_element(*self.confirm_password_field).send_keys(password)

    def accept_terms(self):
        self.driver.find_element(*self.check_box_terms).click()

    def click_create_account_button(self):
        self.driver.find_element(*self.create_account_button).click()

    #Log in:

    def click_log_in(self):
        self.driver.find_element(*self.log_in_button).click()

    def write_user(self, email):
        self.driver.find_element(*self.user_field).send_keys(email)

    def write_user_password(self, password):
        self.driver.find_element(*self.password_user).send_keys(password)

    def click_log_in_user(self):
        self.driver.find_element(*self.log_in_user_button).click()

    #Steps:
    def fill_personal_data(self, name, last_name_one, last_name_two, birthday):
        self.write_name(name)
        self.write_full_last_name(last_name_one, last_name_two)
        self.write_day_of_birth(birthday)

    def fill_contact_data(self, email, phone):
        self.write_email(email)
        self.write_phone(phone)

    def set_password(self, password):
        self.write_password(password)
        self.confirm_password(password)











    

