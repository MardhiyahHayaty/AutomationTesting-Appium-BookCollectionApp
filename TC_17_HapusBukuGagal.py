import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

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
        detail_buku = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.view.ViewGroup')
        detail_buku.click()
        time.sleep(3)

        hapus_button = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnHapusBuku')
        hapus_button.click()
        time.sleep(2)

        tidak_button = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]')
        tidak_button.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()