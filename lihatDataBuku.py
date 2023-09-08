import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.startup.tugas_5_eureka',
    appActivity='com.startup.tugas_5_eureka.ui.activities.splash_screen.SplashScreenActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723/wd/hub'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_soal(self) -> None:
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(545, 1871)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(574, 296)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)
    

        
    

if __name__ == '__main__':
    unittest.main()


