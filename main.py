import json
import asyncio

import src.lib as lib
import src.tui as tui

class maindl():
    def __init__(self):
        pass

    async def run(self):
        options = tui.prompt_options()
        if options == "P":
            driver = lib.find_os()
            driver.get("https://instagram.com")
            tui.prompt_login()
            sec = tui.prompt_scroll()
            aagt_items = lib.cache_links(driver, sec)

            lib.save_links(aagt_items)

            await lib.bundle_downloads(aagt_items)

        elif options == "D":
            print("type in the EXACT filename including spaces, fullstops and the .json at the end: \n"
                  "For example, if your file was in the directory /saved-lists/2022-08-14 13.21.30.092375.json, \n"
                  "you would type '2022-08-14 13.21.30.092375.json'")
            filename = input()
            path = f"saved-lists/{filename}"

            f = open(path)
            links = json.load(f)
            await lib.bundle_downloads(links)

        else:
            print("invalid input")
            return


if __name__ == '__main__':
    maindl = maindl()
    asyncio.run(maindl.run())