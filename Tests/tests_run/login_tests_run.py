import unittest
from selenium import webdriver
from config.test_settings import Test_Settings
from Tests.page_objects import main_page, login_page, my_account_page
from time import sleep

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = Test_Settings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test1_load_main_page(self):
        self.assertTrue(main_page.load_main_page(self.driver))

    def test2_go_to_login_page(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.login_page_visibility(self.driver))

    def test3_correct_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(my_account_page.my_account_page_visibility(self.driver))


    def test4_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login(self.driver))


if __name__ == '__main__':
    unittest.main()