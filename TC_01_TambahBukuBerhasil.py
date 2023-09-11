import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

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
        link_foto_field.send_keys("https://media.npr.org/assets/img/2023/05/02/water_custom-3c24e76a8ab773623dd89fcb25a7e8cc66765c6d-s1100-c50.jpg")

        judul_buku_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etJudulBuku')
        judul_buku_field.send_keys("Bumi")

        nama_penerbit_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etPenerbitBuku')
        nama_penerbit_field.send_keys("Gramedia")

        tahun_terbit_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etTahunTerbit')
        tahun_terbit_field.send_keys("2014")

        kategori_field = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/etKategoriBuku')
        kategori_field.send_keys("Petualangan")

        time.sleep(2)

        tambahbuku_btn = self.driver.find_element(by=AppiumBy.ID, value='com.startup.tugas_5_eureka:id/btnTambahBuku')
        tambahbuku_btn.click()

        time.sleep(3)

        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(507, 1913)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(570, 334)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()