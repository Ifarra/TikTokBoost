import undetected_chromedriver as uc
import platform, os, time
from colorama import Fore
import selenium
from interface.interface import interface

banner = """
Modified by:
██╗███████╗ █████╗ ██████╗ ██████╗  █████╗ 
██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║█████╗  ███████║██████╔╝██████╔╝███████║
██║██╔══╝  ██╔══██║██╔══██╗██╔══██╗██╔══██║
██║██║     ██║  ██║██║  ██║██║  ██║██║  ██║
╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝"""

class holo:
    def __init__(self):
        self.driver = uc.Chrome()
        self.interface = interface()
        self.captcha_box = '/html/body/div[5]/div[2]/form/div/div'
        self.clear       = "clear"
        
        if platform.system() == "Windows":
            self.clear = "cls"
            
        self.color  = Fore.BLUE
        self.sent   = 0
        self.xpaths = {
            "followers"     : "/html/body/div[6]/div/div[2]/div/div/div[2]/div/button",
            "hearts"        : "/html/body/div[6]/div/div[2]/div/div/div[3]/div/button",
            "comment_hearts": "/html/body/div[6]/div/div[2]/div/div/div[4]/div/button",
            "views"         : "/html/body/div[6]/div/div[2]/div/div/div[6]/div/button",
            "shares"        : "/html/body/div[6]/div/div[2]/div/div/div[7]/div/button",
            "favorites"     : "/html/body/div[6]/div/div[2]/div/div/div[8]/div/button",
        }
        self.choice = 0
        self.input  = ""
        self.limit  = 0
        
            
    def main(self):
        try: 
            os.system(self.clear)
            self.interface.change_title("TikTok Booster")
            
            print(self.color + banner)
            print("\n" + self.interface._print("Waiting for Zefoy to load... 502 Error = Blocked country or VPN is on"))
            
            self.driver.get("https://zefoy.com")
            self.wait_for_xpath(self.captcha_box)
            
            print(self.interface._print("Site loaded, enter the CAPTCHA to continue."))
            print(self.interface._print("Waiting for you..."))
            
            self.wait_for_xpath(self.xpaths["followers"])
            os.system(self.clear)
            status = self.check_status()
            
            print(self.color + banner)
            print()
            print(self.interface._print(f"Select your option below." + "\n"))
            
            counter = 1
            for thing in status:
                print(self.interface._print(f"{thing} {status[thing]}", counter))
                counter += 1
            
            print(f" {Fore.WHITE}[{self.color}7{Fore.WHITE}] Set Limit")
            
            option = int(input("\n" + self.interface._print(f"")))
            
            self.user_choice(option)
            
        except Exception:
            self.driver.quit()
            os._exit(1)

    def send_bot(self, search_button, main_xpath, vid_info, div):
        try:            
            element = self.driver.find_element('xpath', main_xpath)
            element.clear()
            element.send_keys(vid_info)
            time.sleep(6)

            find_start = f"/html/body/div[{div}]/div/div/*"
            if not self.driver.find_elements("xpath", find_start):
                self.driver.find_element("xpath", search_button).click()
                time.sleep(5)

            ratelimit_seconds, full = self.check_submit(div)
            if "(s)" in str(full):
                self.main_sleep(ratelimit_seconds)
                self.driver.find_element('xpath', search_button).click()
                time.sleep(5)

            send_button = f'/html/body/div[{div}]/div/div/div[1]/div/form/button'
            button = self.driver.find_element('xpath', send_button)
            count_text = button.text
            button.click()
            self.sent += 1
            print(self.interface._print(f"[ {self.sent} ] | Live value: {count_text}"))

            time.sleep(3)
            count_textv = count_text.replace(',', '')
            self.check_limit(int(count_textv))
            self.send_bot(search_button, main_xpath, vid_info, div)

        except Exception:
            self.driver.refresh()
            self.wait_for_user(self.xpaths["followers"])
            time.sleep(5)
            self.user_choice(self.choice)

    def main_sleep(self, delay):
        while delay != 0:
            time.sleep(1)
            delay -= 1
            self.interface.change_title(f"TikTok Zefoy Automator | Cooldown: {delay}s | Github: @ifarra")

    def convert(self, min, sec):
        seconds = 0
        
        if min != 0:
            answer = int(min) * 60
            seconds += answer
        
        seconds += int(sec) + 5
        return seconds

    def check_submit(self, div):
        remaining = f"/html/body/div[{div}]/div/div/span[1]"
        
        try:
            element = self.driver.find_element("xpath", remaining)
        except:
            return None, None
        
        if "READY" in element.text:
            return True, True
        
        if "seconds for your next submit" in element.text:
            output          = element.text.split("Please wait ")[1].split(" for")[0]
            minutes         = element.text.split("Please wait ")[1].split(" ")[0]
            seconds         = element.text.split("(s) ")[1].split(" ")[0]
            sleep_duration  = self.convert(minutes, seconds)
            
            return sleep_duration, output
        
        return element.text, None
        
    def check_status(self):
        statuses = {}
        
        for thing, value in self.xpaths.items():
            value = self.xpaths[thing]
            element = self.driver.find_element('xpath', value)
            
            if not element.is_enabled():
                statuses[thing] = f"{Fore.RED}[OFFLINE]"
            
            else:
                statuses[thing] = f"{Fore.GREEN}[WORKS]"
        
        return statuses

    

    def wait_for_xpath(self, xpath):
        while True:
            try:
                f = self.driver.find_element('xpath', xpath)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                pass
            
    def wait_for_user(self, xpath):
        print(self.interface._print("Waiting for you..."))
        while True:
            try:
                time.sleep(3)
                f = self.driver.find_element('xpath', xpath)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                pass
            
    def user_choice(self, option):
        if option == 1:
            div = "7"
            self.choice = 1
            self.driver.find_element("xpath", self.xpaths["followers"]).click()
        
        elif option == 2:
            div = "8"
            self.choice = 2
            self.driver.find_element("xpath", self.xpaths["hearts"]).click()
            
        elif option == 3:
            div = "9"
            self.choice = 3
            self.driver.find_element("xpath", self.xpaths["comment_hearts"]).click()
            
        elif option == 4: 
            div = "10"
            self.choice = 4
            self.driver.find_element("xpath", self.xpaths["views"]).click()
            
        elif option == 5:
            div = "11"
            self.choice = 5
            self.driver.find_element("xpath", self.xpaths["shares"]).click()
            
        elif option == 6:
            div = "12"
            self.choice = 6
            self.driver.find_element("xpath", self.xpaths["favorites"]).click()
            
        elif option == 7:
            self.limit = input("\n" + self.interface._print("Enter limit: "))
            os.system(self.clear)
            status = self.check_status()
            
            print(self.color + banner)
            print()
            print(self.interface._print(f"Select your option below." + "\n"))
            print('Limit: ' + self.limit)
            
            counter = 1
            for thing in status:
                print(self.interface._print(f"{thing} {status[thing]}", counter))
                counter += 1
            
            option = int(input("\n" + self.interface._print(f"")))
            
            self.user_choice(option)
        
        else:
            self.driver.quit()
            os._exit(1)
            
        video_url_box = f'/html/body/div[{div}]/div/form/div/input'
        search_box    = f'/html/body/div[{div}]/div/form/div/div/button'
        vid_info = self.input if self.input else input("\n" + self.interface._print("Username/VideoURL: "))
        self.input = vid_info
            
        self.send_bot(search_box, video_url_box, vid_info, div)
        
    def check_limit(self, limit):
        if int(self.limit) > 0 and limit >= int(self.limit):
            print(f"Limit is reached. Limit: {self.limit}")
            self.driver.quit()
            os._exit(1)

if __name__ == "__main__":
    try:
        obj = holo()
        obj.main()
    except Exception as e:
        print("\n" + str(e))
        input("\nPress Enter to exit...")
        os._exit(1)
