from datetime import datetime
import logging
import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time

LOGGER = logging.getLogger(__name__)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://app.parkalot.io/")

driver.implicitly_wait(120)
driver.maximize_window()


def login():
    time.sleep(5)
    username = 'guy.p@minutemedia.com'
    password = 'LizaTheQueen'

    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    assert email_input is not None
    email_input.click()
    email_input.send_keys(username)

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    assert password_input is not None
    password_input.click()
    password_input.send_keys(password + Keys.RETURN)


def login_as_proxy():
    button = driver.find_element(By.XPATH,
                                 '//*[@id="aside"]/div/div[2]/div[1]/div[2]/div/div/div/nav/ul[1]/li[5]/a/span[2]')
    time.sleep(5)
    ActionChains(driver).move_to_element(button).click(button).perform()


def reserve_a_place():
    time.sleep(10)
    button = driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div/div[2]/div[2]/button[3]')

    button.click()
    random_time = random.randint(3, 6)

    random_time = random_time * 100
    time.sleep(random_time)


def exit_proxy_mode():
    exit_proxy_mode_button = driver.find_element(By.XPATH,
                                                 '//*[@id="aside"]/div/div[2]/div[1]/div[2]/div/div/div/nav/ul[1]/li[6]/a/span[2]')
    exit_proxy_mode_button.click()
    time.sleep(10)


def loopOverProxies():
    time.sleep(10)
    list_of_user_proxies = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[5]/div/div/div[2]/div[1]')

    list_options = list_of_user_proxies.find_elements(By.TAG_NAME, "li")

    for idx, user in enumerate(list_options):
        time.sleep(10)
        index = idx + 1

        click_first_proxy = driver.find_element(By.CSS_SELECTOR, f'li.list-item:nth-child({index})')

        click_first_proxy.click()
        reserve_a_place()
        exit_proxy_mode()
        login_as_proxy()


def run_program():
    login()
    login_as_proxy()
    loopOverProxies()


run_program()
