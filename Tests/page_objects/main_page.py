from Tests.helpers.SupportFunctions import *
from time import sleep

taps_shop_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
cart_page_header_link = 'menu-item-99'
my_account_page_header_link = 'menu-item-100'
order_header_link = 'menu-item-101'
shop_header_link = 'menu-item-102'
hoodie_item = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a'
go_to_cart_under_item = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a[2]'
icon_go_to_cart = 'site-header-cart'
cart_status = '//*[@id="site-header-cart"]/li[2]/div/div'

def load_main_page(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance,taps_shop_logo)
    return elem.is_displayed()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, my_account_page_header_link)
    elem = driver_instance.find_element(By.ID, my_account_page_header_link)
    elem.click()


def add_hoodie_to_cart(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, hoodie_item)
    elem = driver_instance.find_element(By.XPATH, hoodie_item)
    elem.click()


def go_to_cart_from_under_item(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, go_to_cart_under_item)
    elem = driver_instance.find_element(By.XPATH, go_to_cart_under_item)
    elem.click()


def go_to_cart_from_header(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, cart_page_header_link)
    elem.click()


def go_to_cart_from_basket_icon(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, icon_go_to_cart)
    elem.click()


def hover_over_cart(driver_instance):
    hover_over_element_by_id(driver_instance, icon_go_to_cart)
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, cart_status)
    if elem.text == 'Brak produktów w koszyku.':
        return True
    else:
        return False


def hover_over_cart_with_element(driver_instance):
    hover_over_element_by_id(driver_instance, icon_go_to_cart)
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, cart_status)
    if elem.text != 'Brak produktów w koszyku.':
        return True
    else:
        return False


