from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


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

    def scroll_down(self, scroll_duration=200):
        size = self.driver.get_window_size()
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.3
        start_x = size ['width'] / 2

        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(scroll_duration / 1000)
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()

        actions.perform()


