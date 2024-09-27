from appium.webdriver.common.appiumby import AppiumBy




class MobileHelpers:

    def __init__(self, driver):
        self.driver = driver


    def scroll_to_text(self, text):
        scrollable = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )
        self.driver.find_element(*scrollable)

    def scroll_to_partial_text(self, partial_text):
        scrollable = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{partial_text}"))'
        )
        self.driver.find_element(*scrollable)







