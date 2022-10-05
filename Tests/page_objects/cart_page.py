from Tests.helpers.SupportFunctions import *

item_in_cart = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]'
remove_item = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]/td[1]'
submit_cart = '//*[@id="post-7"]/div/div/div[2]/div/div/a'
cart_page_title = '//*[@id="post-7"]/header/h1'
empty_cart_info = '//*[@id="post-7"]/div/div'
back_to_shop_button = '//*[@id="post-7"]/div/div/p[2]/a'

def check_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, item_in_cart)
    return elem.is_displayed()


def remove_item_from_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, remove_item)
    elem.click()


def check_remove_item_from_cart(driver_instance):
    try:
        wait_for_invisibility_of_element_by_xpath(driver_instance, remove_item)
        return True
    except: NoSuchElementException
    return False


def approve_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, submit_cart)
    elem.click()


def cart_page_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, cart_page_title)
    return elem.is_displayed()


def empty_cart_alert(driver_instance):
    elem = driver_instance.find_element(By.CSS_SELECTOR, '#post-7 > div > div > p.cart-empty.woocommerce-info')
    if elem.text == 'Twój koszyk aktualnie jest pusty.':
        return True
    else:
        return False


def back_to_shop_from_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, back_to_shop_button)
    elem.click()