import time
import asyncio
import keyboard

import src.lib as lib
import src.tui as tui

class maindl():
    def __init__(self):
        pass

    def scroll_and_f12(self, driver):
        SCROLL_PAUSE_TIME = 0.5

        current_height = driver.execute_script("return document.body.scrollHeight")

        keyboard.press_and_release("F12")
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        return current_height

    async def run(self):
        driver = lib.find_os()
        driver.get("https://godly.website/websites/long-scrolling")
        while True:
            height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(5)
            current_height = self.scroll_and_f12(driver)

            print(current_height)
            print(height)

            if height == current_height:
                break



if __name__ == '__main__':
    maindl = maindl()
    asyncio.run(maindl.run())