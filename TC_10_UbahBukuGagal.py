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
        detail_buku = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup')
        detail_buku.click()
        time.sleep(5)

        ubah_button = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnUbahBuku')
        ubah_button.click()
        time.sleep(2)
        
        ubah_link_foto = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etLinkFotoBuku')
        ubah_link_foto.clear()
        time.sleep(2)
        ubah_link_foto.send_keys("https://booktrib.com/wp-content/uploads/2023/06/The-Covenant-of-Water")
        time.sleep(2)

        ubah_buku_btn = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnYakinUbahBuku')
        ubah_buku_btn.click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()