# coding=utf-8
import logging
import os
import traceback

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def login(chrome, usr_name, pwd):
    logger.info("Login for: %s with pass: %s" % (usr_name, pwd))
    chrome.get("https://stuhealth.jnu.edu.cn/#/login")

    element_usr_id = chrome.find_element_by_name('appId')
    element_usr_id.clear()
    element_usr_id.send_keys(usr_name)

    ele_pass = chrome.find_element_by_id('passw')
    ele_pass.clear()
    ele_pass.send_keys(pwd)

    btn = chrome.find_element_by_xpath("//button")
    btn.click()
    WebDriverWait(chrome, 60, 0.5).until(ec.staleness_of(btn))


def submit(chrome):
    logger.info("Start submit")
    ele = chrome.find_element_by_id("loading")
    WebDriverWait(chrome, 60, 0.5).until(ec.invisibility_of_element(ele))
    # 本人承诺XXX
    ele = chrome.find_element_by_id("10000")
    webdriver.ActionChains(chrome).move_to_element(ele).click(ele).perform()
    # 提交
    ele = chrome.find_element_by_id("tj")
    webdriver.ActionChains(chrome).move_to_element(ele).click(ele).perform()
    WebDriverWait(chrome, 60, 0.5).until(ec.staleness_of(ele))


def is_complete(chrome):
    current_page_url = chrome.current_url
    logger.debug(current_page_url)
    return "complete" in current_page_url


def is_login(chrome):
    current_page_url = chrome.current_url
    logger.debug(current_page_url)
    return "complete" in current_page_url or "index" in current_page_url


def get_chrome_driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)


def set_geo_location(chrome):
    import random
    map_coordinates = dict({
        "latitude": round(22.2522701 + random.random(), 7),
        "longitude": round(113.5296717 + random.random(), 7),
        "accuracy": random.randint(500, 3000)
    })
    chrome.execute_cdp_cmd("Emulation.setGeolocationOverride", map_coordinates)


def save_for(file, message):
    with open(file + ".txt", 'a+', encoding="utf-8") as email:
        email.write(message + '\n')
        email.flush()
        email.close()


def save_for_mail_body(message):
    save_for("body", message)


def save_for_mail_subject(message):
    save_for("subject", message)


driver = webdriver.Chrome()
driver.set_page_load_timeout(60)
driver.implicitly_wait(10)
set_geo_location(driver)

usr_id = os.getenv("USERID")
usr_pwd = os.getenv("USERPASS")
completed = False
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Health Submit")
try:
    login(driver, usr_id, usr_pwd)
    if is_login(driver):
        if not is_complete(driver):
            submit(driver)
        if is_complete(driver):
            completed = True
            save_for_mail_body("Completed!")
except Exception as e:
    logger.error("Failed to submit:\n%s\n" % traceback.format_exc())
    save_for_mail_body("打卡失败\n%s\n" % traceback.format_exc())
driver.quit()
if completed:
    logger.info("User:%s completed" % usr_id)
    save_for_mail_subject("健康申报：成功！\n%s" % usr_id)
else:
    logger.info("User:%s failed" % usr_id)
    save_for_mail_subject("健康申报：失败！\n%s" % usr_id)
