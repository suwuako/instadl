import sys
import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

def find_os():
    """
    gets user os to set driver
    :return: selenium driver
    """
    windows = ["win32"]
    linux = ["linux", "linux2"]
    platform = sys.platform

    path = pathlib.Path().absolute()

    if platform in windows:
        driver_path = fr"{path}\ext\geckodriver.exe"

    elif platform in linux:
        driver_path = fr"{path}.ext.geckodriver"

    else:
        driver_path = fr"{path}.external.geckodriver"

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

def get_links(driver, aagt_items):
    """
    :param driver:
    :param aagt_items:
    :return image_links: list of image links
    """

    image_links = list()

    for i in aagt_items:
        image_links.append(i.get_attribute("src"))

    return image_links