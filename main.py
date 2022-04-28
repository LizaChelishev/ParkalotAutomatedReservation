from datetime import datetime
import logging
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
    USERNAME = 'guy.p@minutemedia.com'
    PASSWORD = 'LizaTheQueen'

    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    assert email_input is not None
    email_input.click()
    email_input.send_keys(USERNAME)

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    assert password_input is not None
    password_input.click()
    password_input.send_keys(PASSWORD + Keys.RETURN)
    time.sleep(5)


def login_as_proxy():
    button = driver.find_element(By.XPATH,
                                 '//*[@id="aside"]/div/div[2]/div[1]/div[2]/div/div/div/nav/ul[1]/li[5]/a/span[2]')
    time.sleep(5)

    time.sleep(5)
    ActionChains(driver).move_to_element(button).click(button).perform()
    time.sleep(5)

    # click_first_proxy = driver.find_element(By.XPATH, "//div[@class='list-body']")
    # click_first_proxy.click()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    # time.sleep(10)


#
# def login_as_proxy_iterable():
#     list_of_user_proxies = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div/div/div[4]/div/div/div[2]/div[1]')
#     for user in list_of_user_proxies:
#         list_of_user_proxies[0].click()

def reserve_a_place():
    time.sleep(10)
    button = driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div/div[2]/div[2]/button[3]')

    button.click()
    time.sleep(10)

def loopOverProxies():
    time.sleep(10)
    list_of_user_proxies = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[5]/div/div/div[2]/div[1]')

    list_options = list_of_user_proxies.find_elements(By.TAG_NAME, "li")

    for idx, user in enumerate(list_options):
        index = idx + 1
        print(index)
        click_first_proxy = driver.find_element(By.CSS_SELECTOR, f'li.list-item:nth-child({index})')

        click_first_proxy.click()
        reserve_a_place()
        exit_proxy_mode()
        login_as_proxy()


def exit_proxy_mode():
    exit_proxy_mode_button = driver.find_element(By.XPATH,
                                                 '//*[@id="aside"]/div/div[2]/div[1]/div[2]/div/div/div/nav/ul[1]/li[6]/a/span[2]')
    exit_proxy_mode_button.click()
    time.sleep(10)


def run_program():
    login()
    login_as_proxy()
    loopOverProxies()
    # reserve_a_place()
    # login_as_proxy()


#     reserve_a_place()
#     exit_proxy_mode()
#     login_as_proxy()
#     reserve_a_place()
#
#
# # def testing_scheduler_functions():
# #     print('You can use functions')
# #
# #
# # def testing_schedule():
# #     print('Scheduler is working')
# #     testing_scheduler_functions()
# #
# #
# # def scheduler_tester():
# #     schedule.every().day.at("13:34").do(testing_schedule)
# #     #schedule.every(1).minutes.do(testing_schedule)
# #     while True:
# #         print('Checking schedule')
# #         schedule.run_pending()
# #         time.sleep(10)
#
#
# def scheduler():
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print("Current Time =", current_time)
#     schedule.every().day.at("18:17").do(run_program)
#
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
#
# #scheduler_tester()
# scheduler()
run_program()
