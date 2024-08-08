import ctypes, platform
from colorama import Fore
class interface:
    def __init__(self):
        self.clear = "clear"
        
        if platform.system() == "Windows":
            self.clear = "cls"
            
        self.color = Fore.BLUE
    def _print(self, msg, status = "-"):
        return f" {Fore.WHITE}[{self.color}{status}{Fore.WHITE}] {msg}"

    def change_title(self, arg):
        if self.clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW(arg)