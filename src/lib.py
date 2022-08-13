import sys
import pathlib

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def find_os():
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