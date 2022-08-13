import time
import requests
import shutil

import src.lib as lib
import src.tui as tui

class maindl():
    def __init__(self):
        pass

    def run(self):
        driver = lib.find_os()
        link = "https://scontent-nrt1-1.cdninstagram.com/v/t51.2885-15/298413458_1450823602056729_2300657221757228720_n.jpg?stp=dst-jpg_e15_fr_p1080x1080&_nc_ht=scontent-nrt1-1.cdninstagram.com&_nc_cat=109&_nc_ohc=K5qthe_V19sAX9NDD4K&tn=JK28nsAeOT9zjV2_&edm=ACOOH6wBAAAA&ccb=7-5&ig_cache_key=MjkwMjE0OTUxNzIyOTE4MzAzNQ%3D%3D.2-ccb7-5&oh=00_AT-wWVqgp1hAZnk0OJzx7b1UQERGmSeulcR2oPfDL4kqxw&oe=62FF7B63&_nc_sid=ec1c8f"

        driver.get(link)
        # tui.prompt_login()
        # aagt_items = lib.find_aagt(driver)
        # image_links = lib.get_links(aagt_items)
        # lib.download_links(driver, image_links)

        res = requests.get(link, stream = True)
        with open("test", 'wb') as f:
            shutil.copyfileobj(res.raw, f)

if __name__ == '__main__':
    maindl = maindl()
    maindl.run()

