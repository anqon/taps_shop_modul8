import unittest
from selenium import webdriver
from config.test_settings import Test_Settings
from Tests.page_objects import main_page, login_page, my_account_page, cart_page,shop_page,search_element_check_details
from time import sleep

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = Test_Settings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

#More login tests

    def test1_forgotten_password_empty_email(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.login_page_visibility(self.driver))
        login_page.forgotten_password_click(self.driver)
        self.assertTrue(login_page.forgotten_password_site_visible(self.driver))
        login_page.forgotten_password_empty_email_reset_button(self.driver)
        self.assertTrue(login_page.validate_forgotten_password_empty_email(self.driver))

    def test10_forgotten_password_correct_message(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.login_page_visibility(self.driver))
        login_page.forgotten_password_click(self.driver)
        login_page.send_email_to_reminder_password(self.driver)
        self.assertTrue(login_page.validate_correct_reset_password(self.driver))


#More cart tests
    def test_go_to_cart_from_header_link(self):
        main_page.go_to_cart_from_header(self.driver)
        self.assertTrue(cart_page.cart_page_visible(self.driver))

    def test_go_to_cart_from_basket_icon(self):
        main_page.go_to_cart_from_basket_icon(self.driver)
        self.assertTrue(cart_page.cart_page_visible(self.driver))


    def test_cart1_empty_cart_alert_visible(self):
        main_page.go_to_cart_from_header(self.driver)
        self.assertTrue(cart_page.empty_cart_alert(self.driver))

    def test_back_from_cart_to_shop(self):
        main_page.go_to_cart_from_header(self.driver)
        cart_page.back_to_shop_from_cart(self.driver)
        self.assertTrue(shop_page.shop_site_visibility(self.driver))

    def test_hoover_over_basket_to_visible_empty_info(self):
        self.assertTrue(main_page.hover_over_cart(self.driver))

    def test_hover_over_basket_with_hoodie(self):
        main_page.load_main_page(self.driver)
        main_page.add_hoodie_to_cart(self.driver)
        self.assertTrue(main_page.hover_over_cart_with_element(self.driver))


#test for shop element details
    def test_search_field_result_for_cap(self):
        search_element_check_details.search_field_test_cap(self.driver)
        self.assertTrue(search_element_check_details.search_field_result(self.driver))

    def test_element_additional_information(self):
        search_element_check_details.search_field_test_cap(self.driver)
        search_element_check_details.click_additional_information(self.driver)
        self.assertTrue(search_element_check_details.additional_information_section_visibility(self.driver))

    def test_element_opinions(self):
        search_element_check_details.search_field_test_cap(self.driver)
        search_element_check_details.click_opinions(self.driver)
        self.assertTrue(search_element_check_details.opinions_section_visibility(self.driver))
        sleep(2)

    def test_element_opinion_empty_stars_alert(self):
        search_element_check_details.search_field_test_cap(self.driver)
        search_element_check_details.click_opinions(self.driver)
        search_element_check_details.add_opinion_empty_stars_alert(self.driver)
        sleep(3)

    def test_element_add_correct_opinion(self):
        search_element_check_details.search_field_test_cap(self.driver)
        search_element_check_details.click_opinions(self.driver)
        search_element_check_details.add_correct_opinion(self.driver)
        sleep(15)
        self.assertTrue(search_element_check_details.add_correct_opinion_validation(self.driver))
        sleep(3)
if __name__ == '__main__':
    unittest.main()