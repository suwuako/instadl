import sys
import time
import pathlib
import requests
import shutil
import random
import asyncio
import keyboard
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
    aagt_items = driver.find_elements(By.CLASS_NAME, "_aagt")

    return aagt_items


def get_link(aagt):
    """
    :param aagt: webdriver aagt element
    :return image_links: list of image links
    """

    return aagt.get_attribute("src")

def cache_links(driver):
    saved_aagt = []
    saved_links = []
    count = 1
    while True:
        print("searching...")
        aagt = find_aagt(driver)

        for i in aagt:
            if i not in saved_aagt:
                print(f"[{count}] getting link...")
                saved_aagt.append(i)
                saved_links.append(get_link(i))
                count += 1

        print(f"loaded {len(saved_aagt)} items and loaded {len(saved_links)} links... ")

        if keyboard.read_key() == "p":
            return saved_links


async def download_links(image_links):
    """
    :param driver: selenium driver
    :param prefs:  firefox preferences
    :param image_links: list of image links
    :return:
    """
    print(f"started main at {time.strftime('%X')}")
    print(f"DOWNLOADING [{len(image_links)}] IMAGES")

    # So idk why it decides to kill itself, my best asusmption is that its because i pass args into dl().
    # Can someone smarter than me fix & pull request ty <3
    try:
        await asyncio.gather(
            *(asyncio.to_thread(dl(i, image_links)) for i in image_links)
        )
    except:
        print(f"finished main at {time.strftime('%X')}")

def dl(link, image_links):
    OUTPUT_PATH = "output/"
    file_extension = "png"
    count = 1
    res = requests.get(link, stream=True)
    download_path = f"{OUTPUT_PATH}{random.randint(10000000, 99999999)}.{file_extension}"

    if res.status_code == 200:
        print(f"[{image_links.index(link)+1}]downloading image...")
        with open(download_path, 'wb') as f:
            shutil.copyfileobj(res.raw, f)

    else:
        print("File could not be downloaded")

        count += 1