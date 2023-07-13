import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/dona/Documents/chromedriver"

chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")



while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    cursor = driver.find_element(By.ID, "buyCursor")
    grandma = driver.find_element(By.ID, "buyGrandma")
    factory = driver.find_element(By.ID, "buyFactory")
    mine = driver.find_element(By.ID, "buyMine")
    shipment = driver.find_element(By.ID, "buyShipment")
    alechemy = driver.find_element(By.ID, "buyAlchemy lab")
    portal = driver.find_element(By.ID, "buyPortal")
    timemac = driver.find_element(By.ID, "buyTime machine")


    if timemac.get_attribute("class") == "":
        timemac.click()
    elif portal.get_attribute("class") == "":
        portal.click()
    elif alechemy.get_attribute("class") == "":
        alechemy.click()
    elif shipment.get_attribute("class") == "":
        shipment.click()
    elif mine.get_attribute("class") == "":
        mine.click()
    elif factory.get_attribute("class") == "":
        factory.click()
    elif grandma.get_attribute("class") == "":
        grandma.click()
    elif cursor.get_attribute("class") == "":
        cursor.click()








driver.quit()