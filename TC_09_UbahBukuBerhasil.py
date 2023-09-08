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
        
        ubah_judul = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etJudulBuku')
        ubah_judul.clear()
        time.sleep(1)
        ubah_judul.send_keys("Rembulan di Wajahmu")
        time.sleep(2)

        ubah_penerbit = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etPenerbitBuku')
        ubah_penerbit.clear()
        time.sleep(1)
        ubah_penerbit.send_keys("Gramedia")
        time.sleep(2)

        ubah_tahun = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etTahunTerbit')
        ubah_tahun.clear()
        time.sleep(1)
        ubah_tahun.send_keys("2020")
        time.sleep(2)

        ubah_kategori = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etKategoriBuku')
        ubah_kategori.clear()
        time.sleep(1)
        ubah_kategori.send_keys("Romansa")
        time.sleep(2)

        ubah_buku_btn = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnYakinUbahBuku')
        ubah_buku_btn.click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()