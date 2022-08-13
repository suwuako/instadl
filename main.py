import time

import src.lib as lib
import src.tui as tui

class maindl():
    def __init__(self):
        pass

    def run(self):
        driver = lib.find_os()

        driver.get("https://instagram.com")
        tui.prompt_login()
        aagt_items = lib.find_aagt(driver)
        image_links = lib.get_links(aagt_items)
        lib.download_links(driver, image_links)


if __name__ == '__main__':
    maindl = maindl()
    maindl.run()