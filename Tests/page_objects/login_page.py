from Tests.helpers.SupportFunctions import *
from Tests.helpers.DataGenerator import *


login_header = '//*[@id="customer_login"]/div[1]/h2'
username = 'username'
password = 'password'
login_button = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
rememberme = 'rememberme'
wrong_password = '1234'
login_error_info = '//*[@id="content"]/div/div[1]/ul/li[1]'

propper_email1 = 'cotaga1249@maillei.net'
propper_password1 = 'VRrMhK8MqFyd'

propper_email2 = 'wowen49501@maillei.net'
propper_password2 = 'lxsg#GAqH$Ke'

propper_email3 = 'bomineg967@onmail3.com'
propper_password3 = 'zedvu@##)CZy'

propper_email4 = 'wacog70401@tinkmail.net'
propper_password4 = 'Lk*3Q9&am3zL'

propper_email5 = 'calose2528@maillei.net'
propper_password5 = 'lkSb&SAJwLWo'

reset_password_link = 'Nie pamiętasz hasła?'
forgotten_password_site_header = '//*[@id="post-9"]/header/h1'
reset_password_button = '//*[@id="post-9"]/div/div/form/p[3]/button'
reset_wrong_message = '//*[@id="content"]/div/div[1]'
reset_email_field = 'user_login'
reset_correct_message = '//*[@id="post-9"]/div/div/div'

def login_page_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, login_header)
    return elem.is_displayed()


def correct_login(driver_instance):
    elem = driver_instance.find_element(By.ID, username)
    elem.send_keys(propper_email1)
    elem1 = driver_instance.find_element(By.ID, password)
    elem1.send_keys(propper_password1)
    elem2 = driver_instance.find_element(By.XPATH, login_button)
    elem2.click()


def incorrect_login(driver_instance):
    elem = driver_instance.find_element(By.ID, username)
    elem.send_keys(DataGenerator.generateProperEmail())
    elem1 = driver_instance.find_element(By.ID, password)
    elem1.send_keys(wrong_password)
    elem2 = driver_instance.find_element(By.XPATH, login_button)
    elem2.click()
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, login_error_info)
        return elem2.is_displayed()
    except StaleElementReferenceException:
        print('Error wrong username/password')
        return True


def forgotten_password_click(driver_instance):
    elem = driver_instance.find_element(By.LINK_TEXT, reset_password_link)
    elem.click()


def forgotten_password_site_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, forgotten_password_site_header)
    return elem.is_displayed()


def forgotten_password_empty_email_reset_button(driver_instance):
    elem = driver_instance.find_element(By.XPATH, reset_password_button)
    elem.click()


def validate_forgotten_password_empty_email(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, reset_wrong_message)
    return elem.is_displayed()


def send_email_to_reminder_password(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance,reset_email_field)
    elem = driver_instance.find_element(By.ID, reset_email_field)
    elem.send_keys(DataGenerator.generateProperEmail())
    elem1 = driver_instance.find_element(By.XPATH, reset_password_button)
    elem1.click()


def validate_correct_reset_password(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, reset_correct_message)
    if elem.text == 'Wysłano e-mail do zresetowania hasła.':
        return True
    else:
        return False
