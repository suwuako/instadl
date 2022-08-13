import time

import src.lib as lib
import src.tui as tui

class maindl():
    def __init__(self):
        pass

    def run(self):
        driver = lib.find_os()
        driver.get("https://www.instagram.com/")
        tui.prompt_login()
        aagt_items = lib.find_aagt(driver)
        lib.get_links(driver, aagt_items)


if __name__ == '__main__':
    maindl = maindl()
    maindl.run()

