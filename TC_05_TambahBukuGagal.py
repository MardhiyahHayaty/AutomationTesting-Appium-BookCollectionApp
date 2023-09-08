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
        tambah_button = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnTambahBukuLayoutDaftar')
        tambah_button.click()

        time.sleep(2)

        link_foto_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etLinkFotoBuku')
        link_foto_field.send_keys("https://s3-ap-southeast-1.amazonaws.com/ebook-previews/42717/156292/1.jpg")

        judul_buku_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etJudulBuku')
        judul_buku_field.send_keys("Komet")

        nama_penerbit_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etPenerbitBuku')
        nama_penerbit_field.send_keys("Gramedia")

        tahun_terbit_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etTahunTerbit')
        tahun_terbit_field.send_keys("2035")

        kategori_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etKategoriBuku')
        kategori_field.send_keys("Petualangan")

        time.sleep(2)

        tambahbuku_btn = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnTambahBuku')
        tambahbuku_btn.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()