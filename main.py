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
        sec = tui.prompt_scroll()
        aagt_items = lib.cache_links(driver, sec)

        await lib.download_links(aagt_items)


if __name__ == '__main__':
    maindl = maindl()
    asyncio.run(maindl.run())