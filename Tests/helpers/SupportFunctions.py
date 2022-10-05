from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element_by_xpath(driver_instance, xpath):
    elem = driver_instance.find_element(By.XPATH, xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def hover_over_element_by_id(driver_instance, id):
    elem = driver_instance.find_element(By.ID, id)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def wait_for_visibility_of_element_by_xpath(driver_instance, xpath, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_id(driver_instance, id, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_class_name(driver_instance, class_name, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element_by_xpath(driver_instance, xpath, time_to_wait=8):
    inv_elem = WebDriverWait(driver_instance,time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_elem


def wait_for_clicable_of_element_by_xpath(driver_instance, xpath, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_clicable_of_element_by_id(driver_instance, id, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.element_to_be_clickable((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem