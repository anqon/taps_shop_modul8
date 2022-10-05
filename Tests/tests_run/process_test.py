import unittest
from selenium import webdriver
from config.test_settings import Test_Settings
from Tests.page_objects import main_page, login_page, my_account_page,cart_page,order_page
from time import sleep

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = Test_Settings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test1_correct_process_test(self):
        self.assertTrue(main_page.load_main_page(self.driver))
        main_page.add_hoodie_to_cart(self.driver)
        main_page.go_to_cart_from_uder_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        self.assertTrue(order_page.order_page_visible(self.driver))
        order_page.propper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.check_submit_order(self.driver))


    def test2_wrong_process_test(self):
        self.assertTrue(main_page.load_main_page(self.driver))
        main_page.add_hoodie_to_cart(self.driver)
        main_page.go_to_cart_from_uder_item(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        self.assertTrue(order_page.order_page_visible(self.driver))
        order_page.wrong_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.check_wrong_submit_order(self.driver))



if __name__ == '__main__':
    unittest.main()