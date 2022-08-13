import src.lib as lib

class maindl():
    def __init__(self):
        pass

    def run(self):
        driver = lib.find_os()
        driver.get("https://instagram.com/")


if __name__ == '__main__':
    maindl = maindl()
    maindl.run()

