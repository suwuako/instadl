import pathlib
import sys

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Scrapping old code from old projects i have no idea what these values are
windows = ["win32"]
linux = ["linux", "linux2"]
platform = sys.platform

path = pathlib.Path().absolute()

if platform in windows:
    driver = fr"{path}\ext\geckodriver.exe"
elif platform in linux:
    driver = fr"{path}.external.geckodriver"
else:
    driver = fr"{path}.external.geckodriver"

driver = webdriver.Firefox(service=Service(driver))
driver.get("https://www.instagram.com")

print("login or something")
input("after logging in press enter to continue")

# Not sure if these values chnage also this is really bad i literally hardcoded in a path bruh fix this when possible
username_xpath = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a"
username_class = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _aak1 _a6hd"


print("attempting to find username with xpath")
username = driver.find_element(By.XPATH, username_xpath)
print("success")

print(username)

# Navigate to saved url
driver.get(f"https://www.instagram.com/{username}/saved")

driver.close()