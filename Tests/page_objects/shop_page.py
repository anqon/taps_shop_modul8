from Tests.helpers.SupportFunctions import *


shop_header = '//*[@id="main"]/header/h1'

def shop_site_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, shop_header)
    return elem.is_displayed()