from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MobileHelpers:

    def __init__(self, driver):
        self.driver = driver


    def scroll_to_text(self, text):
        scrollable = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )
        self.driver.find_element(*scrollable)







