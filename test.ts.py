import platform, os, time, requests
from colorama import Fore
import selenium
from selenium.webdriver.chrome.options import Options as options
from selenium.webdriver.common.by import By
import sys

class holo:
    def __init__(self):
        chrome_options = options()
        chrome_options.add_argument('--log-level=1')
        chrome_options.add_argument('--incognito')
        
        self.driver = selenium.webdriver.Chrome(options=chrome_options)

    def main(self):
        self.driver.get("https://zefoy.com")
        
        import time

        # Sleep for a few seconds before closing
        time.sleep(300)
        self.driver.quit()

        

if __name__ == "__main__":

    obj = holo()
    obj.main()
   
