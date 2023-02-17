from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import sys

# import chromedriver_binary
browser = webdriver.Chrome('./chromedriver.exe')

def undergradAsst():
    browser.get('https://courses.hamptonu.edu')
    time.sleep(random.randrange(3, 6))

    browser.find_element_by_id("agree_button").click()


    uName = browser.find_element_by_id("user_id")
    pWord = browser.find_element_by_id("password")

    uName.send_keys("0")
    uName.send_keys("0")
    uName.send_keys("3")
    uName.send_keys("8")
    uName.send_keys("0")
    uName.send_keys("8")
    uName.send_keys("7")
    uName.send_keys("1")

    pWord.send_keys("1")
    pWord.send_keys("5")
    pWord.send_keys("F")
    pWord.send_keys("r")
    pWord.send_keys("e")
    pWord.send_keys("e")
    pWord.send_keys("m")
    pWord.send_keys("a")
    pWord.send_keys("n")

    browser.find_element_by_id("entry-login").click()

    browser.get('https://courses.hamptonu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_215_1')
    browser.send_keys(Keys.CONTROL + 't')
    
# METHOD THAT WAITS FOR A VOCAL SEARCH (aLEXa FUNCTION)
def waitForVocalSearch():
    # extension = "vocalSearchE"
    # domain = "vocalSearchD"
    # subdomain = "vocalSearchS"
    # wait for the vocal search to load
    # browser.get(f'https://{extension}.{domain}.{subdomain}/')

    # Using a while true, but the real question is how to call attention
    # back to running python during browser execution
    # (quite a wonder how python, javascript, html, css, and god
    # knows what other languages are working with this program)

    # while True:
    

    return

def driverUpdate():
    # Open a new window
    browser.execute_script("window.open('');")
    
    # Switch to the new window and open URL B
    browser.switch_to.window(browser.window_handles[1])

    browser.get('https://chromedriver.chromium.org/downloads')
    time.sleep(random.randrange(3, 6))

    # …Do something here
    print("Current Page Title is : %s" %browser.title)
    
        
    lateSt_update = browser.find_element_by_class_name("XqQF9c")
    lateSt_update.click()
    
    time.sleep(random.randrange(6, 9))
    windowsDriver = "/100.0.4896/chromedriver_win32.zip"
    d_load = browser.find_element_by_xpath('//a[@href="'+windowsDriver+'"]')
    d_load.click()

    # Close the tab with URL B
    browser.close()
    
    # Switch back to the first tab with URL A
    browser.switch_to.window(browser.window_handles[0])
    print("Current Page Title is : %s" %browser.title)

    return

def googleLookUp(line):
    browser.get("https://www.google.com/")
    lookup = browser.find_element_by_class_name("gLFyf.gsfi")
    lookup.click()
    
    for c in line:
        lookup.send_keys(c)

    ent = browser.find_element_by_class_name("gNO89b")
    ent.click()

def main():
    undergradAsst()
##    #New Tab
##    browser.send_keys(Keys.CONTROL + 't')
    # driverUpdate()
    goAlt = False
    while True:
        if goAlt:
            # New Tab
            browser.send_keys(Keys.CONTROL + 't')
        inputLine = str(input("Google search\n> "))
        if inputLine == ':q!':
            sys.exit()
        googleLookUp(inputLine)
        goAlt = True

if __name__ == "__main__":
    main()
