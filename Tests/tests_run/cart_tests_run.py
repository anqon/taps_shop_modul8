import unittest
from selenium import webdriver
from config.test_settings import Test_Settings
from Tests.page_objects import main_page, login_page, my_account_page,cart_page
from time import sleep

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = Test_Settings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test1_add_hoodie_item_to_cart(self):
        main_page.add_hoodie_to_cart(self.driver)
        main_page.go_to_cart_from_under_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))

    def test2_remove_item_from_cart(self):
        main_page.add_hoodie_to_cart(self.driver)
        main_page.go_to_cart_from_under_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_remove_item_from_cart(self.driver))

if __name__ == '__main__':
    unittest.main()