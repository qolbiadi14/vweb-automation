from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataSupplierPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_data_poli(self):
        # Implementasi navigasi ke halaman data poli
        pass

    def click_tambah(self):
        tambah_button = self.driver.find_element(By.ID, "tambah_button_id")
        tambah_button.click()

    def fill_field(self, field_name, value):
        field = self.driver.find_element(By.NAME, field_name)
        field.clear()
        field.send_keys(value)

    def click_simpan(self):
        simpan_button = self.driver.find_element(By.ID, "simpan_button_id")
        simpan_button.click()

    def is_supplier_added(self):
        # Implementasi pengecekan apakah data supplier berhasil ditambahkan
        pass