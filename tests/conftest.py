import pytest
from appium.webdriver.appium_service import AppiumService
from appium_config import APPIUM_HOST, APPIUM_PORT

@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()
