import sys
import pathlib
import requests
import shutil
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
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

def get_links(aagt_items):
    """
    :param aagt_items: list of all selenium webelements w/ class _aagt
    :return image_links: list of image links
    """

    image_links = list()

    for i in aagt_items:
        image_links.append(i.get_attribute("src"))

    return image_links

def download_links(driver, image_links):
    """
    :param driver: selenium driver
    :param prefs:  firefox preferences
    :param image_links: list of image links
    :return:
    """

    OUTPUT_PATH = "output/"
    file_extension = "png"
    count = 1

    for i in image_links:
        print(f"[{count}] downloading picture... ({i})")
        res = requests.get(i, stream=True)
        if res.status_code == 200:

            with open(f"{OUTPUT_PATH}{random.randint(10000000,99999999)}.{file_extension}", 'wb') as f:
                shutil.copyfileobj(res.raw, f)

        else:
            print("File could not be downloaded")

        count += 1
