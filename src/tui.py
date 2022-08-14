import time

def prompt_login():
    """
    literally just serves as a thing to wait for user to login before continuing with the program
    :return: null
    """
    print("login to instagram, navigate to your saved page and press enter: ")
    print("Note: the url should look something like 'https://instagram.com/username/saved/all-posts/")
    input()

    return

def prompt_scroll():
    """
    Because instagram only loads 57 images at a time, this is a workaround to cache all the links while the user scrolls down
    :return: null
    """
    print("So because instagram is cringe and will only load 57 images at a time, you will have to wait for the browser"
          "to load all the images"
          "It *should* automatically figure out when it's done scrolling down"
          ""
          "Remember that you NEED to have the browser window highlighted or selected because I can't figure out how to"
          "open inspect element, so keypresses are simulated instead.")
    out = int(input("Because we are loading the images client side, you will have to enter the probable max amount of "
                    "seconds for instagram to load new images. (type a whole number in): "))
    input("Press enter and tab into the browser window")

    for i in range(5):
        print(f"starting in [{5-i}]")
        time.sleep(1)

    print("starting loader...")
    return out

def prompt_options():
    print("Do you want to download from a previously saved json file in 'saved-lists/something.json' or pull from your"
          "instagram feed?")
    return input("(D for download from file, P for pull from instagram)").upper()
