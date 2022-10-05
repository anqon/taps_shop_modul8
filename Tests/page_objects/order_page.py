from Tests.helpers.SupportFunctions import *
from Tests.helpers.DataGenerator import *
from selenium.webdriver.support.ui import Select



order_page_header = '//*[@id="post-8"]/header/h1'
name = 'billing_first_name'
last_name = 'billing_last_name'
country = 'billing_country'
street = 'billing_address_1'
postcode = 'billing_postcode'
city = 'billing_city'
phone = 'billing_phone'
email = 'billing_email'
buy_and_pay_button = 'place_order'

valid_postcode = '00-123'
invalid_postcode = 'abc'

order_confirmation = '//*[@id="post-8"]/header/h1'
order_error = '//*[@id="post-8"]/div/div/form[3]/div[1]/ul'


def order_page_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance,order_page_header)
    return elem.is_displayed


def form_add_propper_name(driver_instance):
    elem = driver_instance.find_element(By.ID, name)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_name(driver_instance):
    elem = driver_instance.find_element(By.ID, name)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_propper_last_name(driver_instance):
    elem = driver_instance.find_element(By.ID, last_name)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_last_name(driver_instance):
    elem = driver_instance.find_element(By.ID, last_name)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def country_drop_down_list(driver_instance):
    elem_list = Select(driver_instance.find_element(By.ID, country))
    wait_for_visibility_of_element_by_id(driver_instance, country, time_to_wait=1)
    elem_list.select_by_index(1)


def form_add_propper_street(driver_instance):
    elem = driver_instance.find_element(By.ID, street)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_street(driver_instance):
    elem = driver_instance.find_element(By.ID, street)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_propper_city(driver_instance):
    elem = driver_instance.find_element(By.ID, city)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_city(driver_instance):
    elem = driver_instance.find_element(By.ID, city)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))

def form_add_propper_postcode(driver_instance):
    elem = driver_instance.find_element(By.ID, postcode)
    elem.send_keys(valid_postcode)


def form_add_wrong_postcode(driver_instance):
    elem = driver_instance.find_element(By.ID, postcode)
    elem.send_keys(invalid_postcode)


def form_add_propper_phone(driver_instance):
    elem = driver_instance.find_element(By.ID, phone)
    elem.send_keys(DataGenerator.generateProperMobileNumber(DataGenerator))


def form_add_wrong_phone(driver_instance):
    elem = driver_instance.find_element(By.ID, phone)
    elem.send_keys(DataGenerator.generateWrongMobileNumber(DataGenerator()))

def form_add_propper_email(driver_instance):
    elem = driver_instance.find_element(By.ID, email)
    elem.send_keys(DataGenerator.generateProperEmail())


def form_add_wrong_email(driver_instance):
    elem = driver_instance.find_element(By.ID, email)
    elem.send_keys(DataGenerator.generateWrongEmail())

def propper_fill_all_form_areas(driver_instance):
    form_add_propper_name(driver_instance)
    form_add_propper_last_name(driver_instance)
    country_drop_down_list(driver_instance)
    form_add_propper_street(driver_instance)
    form_add_propper_postcode(driver_instance)
    form_add_propper_city(driver_instance)
    form_add_propper_phone(driver_instance)
    form_add_propper_email(driver_instance)


def wrong_fill_all_form_areas(driver_instance):
    form_add_wrong_name(driver_instance)
    form_add_wrong_last_name(driver_instance)
    country_drop_down_list(driver_instance)
    form_add_wrong_street(driver_instance)
    form_add_wrong_postcode(driver_instance)
    form_add_wrong_city(driver_instance)
    form_add_wrong_phone(driver_instance)
    form_add_wrong_email(driver_instance)

def submit_order(driver_instance):
    elem = driver_instance.find_element(By.ID, buy_and_pay_button)
    elem.click()


def check_submit_order(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, order_confirmation)
    return elem.is_displayed()


def check_wrong_submit_order(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, order_error)
    return elem.is_displayed()