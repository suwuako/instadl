import sys
import time
import pathlib
import requests
import shutil
import random
import asyncio
import keyboard
import datetime
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox import options

def find_os():
    """
    gets user os to set driver
    :return: dict of drifver and prefs
    """
    windows = ["win32"]
    linux = ["linux", "linux2"]
    platform = sys.platform
    options = webdriver.FirefoxOptions()

    path = pathlib.Path().absolute()

    # Not sure if fr"{path}.output works for linux
    if platform in windows:
        driver_path = fr"{path}\ext\geckodriver.exe"
        option_path = fr"{path}\output"

    elif platform in linux:
        driver_path = fr"{path}.ext.geckodriver"
        option_path = fr"{path}.output"

    else:
        driver_path = fr"{path}.external.geckodriver"
        option_path = fr"{path}.output"

    prefs = {"download.default_directory": option_path}
    driver = webdriver.Firefox(service=Service(driver_path))

    return driver


def find_aagt(driver):
    """
    _aatg is the tag that is used to point to the link that holds the image on instagram's saved posts
    (i dont know if this is just saved posts or it applies to other stuff)
    :param driver: selenium driver
    :return aagt_items: list of selenium webelements
    """
    keyboard.press_and_release("F12")
    aagt_items = driver.find_elements(By.CLASS_NAME, "_aagt")
    keyboard.press_and_release("F12")

    return aagt_items


def get_link(aagt):
    """
    :param aagt: webdriver aagt element
    :return image_links: list of image links
    """

    return aagt.get_attribute("src")


def scroll_and_f12(driver):
    SCROLL_PAUSE_TIME = 0.5

    keyboard.press_and_release("F12")
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    return

def cache_links(driver, load_seconds):
    """
    :param driver:
    :return:
    """

    saved_aagt = []
    saved_links = []

    count = 1

    while True:
        print("searching...")

        height = driver.execute_script("return document.body.scrollHeight")

        keyboard.press_and_release("F12")
        aagt = find_aagt(driver)

        print("_aagt classes found!")

        for i in aagt:
            if i not in saved_aagt:
                print(f"[{count}] getting link...")
                saved_aagt.append(i)
                saved_links.append(get_link(i))
                count += 1

        print(f"loaded {len(saved_aagt)} items and loaded {len(saved_links)} links... ")

        scroll_and_f12(driver)
        time.sleep(load_seconds)

        current_height = driver.execute_script("return document.body.scrollHeight")

        print(f"current page height: {height}")
        print(f"load page height: {current_height}")

        if height == current_height:
            return saved_links


def dl(link, image_links):
    OUTPUT_PATH = "output/"
    file_extension = "png"

    res = requests.get(link, stream=True)
    download_path = f"{OUTPUT_PATH}{random.randint(10000000, 99999999)}.{file_extension}"

    if res.status_code == 200:
        print(f"[PROCESS {image_links.index(link)+1}] Downloading image...")
        with open(download_path, 'wb') as f:
            shutil.copyfileobj(res.raw, f)

    else:
        print("File could not be downloaded")


async def bundle_downloads(links):

    await asyncio.gather(
        *(asyncio.to_thread(dl, links[num], links) for num in range(len(links)))
    )

def save_links(link_list):
    """
    :param link_list:
    :return:
    """

    current_date_and_time = str(datetime.datetime.now()).replace(":", ".")

    with open(f"saved-lists/{current_date_and_time}.json", 'w') as f:
        json.dump(link_list, f, ensure_ascii=False, indent=4)

    print("debug list saved!")