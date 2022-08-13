import time
import asyncio

import src.lib as lib
import src.tui as tui

class maindl():
    def __init__(self):
        pass

    async def run(self):
        driver = lib.find_os()

        driver.get("https://instagram.com")
        tui.prompt_login()
        aagt_items = lib.find_aagt(driver)
        image_links = lib.get_links(aagt_items)
        await lib.download_links(image_links)


if __name__ == '__main__':
    maindl = maindl()
    asyncio.run(maindl.run())