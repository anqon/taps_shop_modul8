from Tests.helpers.SupportFunctions import *


order_made = '//*[@id="post-9"]/div/div/div/p[1]'

def my_account_page_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, order_made)
    return elem.is_displayed()