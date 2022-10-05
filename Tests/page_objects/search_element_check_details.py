from selenium.webdriver import Keys
from Tests.helpers.SupportFunctions import *
from Tests.helpers.DataGenerator import *
from time import sleep

search = 'woocommerce-product-search-field-0'
element_xpath = '//*[@id="product-48"]/div[2]/h1'
additional_information_button = 'tab-title-additional_information'
additional_information_section = '//*[@id="tab-additional_information"]/h2'
opinions_button = 'tab-title-reviews'
opinions_section = '//*[@id="comments"]/h2'
submit_opinion = 'submit'


def search_field_test_cap(driver_instance):
    elem = driver_instance.find_element(By.ID, search)
    elem.send_keys('Cap')
    elem.send_keys(Keys.ENTER)


def search_field_result(driver_instance):
    elem = driver_instance.find_element(By.XPATH, element_xpath )
    elem1 = elem.text
    if elem1 == 'Cap':
        return True
    else:
        return False


def click_additional_information(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, additional_information_button)
    elem = driver_instance.find_element(By.ID, additional_information_button)
    elem.click()


def additional_information_section_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, additional_information_section)
    return elem.is_displayed

def click_opinions(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, opinions_button)
    elem = driver_instance.find_element(By.ID, opinions_button)
    elem.click()


def opinions_section_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, opinions_section)
    return elem.is_displayed


def add_opinion_empty_stars_alert(driver_instance):
    elem = driver_instance.find_element(By.ID, submit_opinion)
    elem.click()
    elem1 = driver_instance.switch_to.alert.text
    if elem1 == 'Proszę wybrać ocenę':
        driver_instance.switch_to.alert.accept()
    else:
        return False

def add_correct_opinion(driver_instance):
    elem = driver_instance.find_element(By.XPATH, '//*[@id="commentform"]/div/p/span/a[4]')
    elem.click()
    elem1 = driver_instance.find_element(By.ID, 'comment')
    elem1.send_keys(DataGenerator.generateProperName())
    elem2 = driver_instance.find_element(By.ID, 'author')
    elem2.send_keys(DataGenerator.generateProperName())
    elem3 = driver_instance.find_element(By.ID, 'email')
    elem3.send_keys(DataGenerator.generateProperEmail())
    elem4 = driver_instance.find_element(By.ID, submit_opinion)
    elem4.click()

def add_correct_opinion_validation(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, '//*[@id="comment-68"]/div/p/em')
    return elem.is_displayed()