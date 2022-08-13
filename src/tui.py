import src.lib as lib

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
    print("So because instagram is cringe and will only load 57 images at a time, you will have to scroll down manually")
    print("Once you are done, press 'p' on your keyboard")
    input("Press enter and then start scrolling down to the bottom.")
