from os import system
import colorama
from colorama import Fore
# autoreset = true, convert ascii = true, DON'T CHANGE OR WILL MESS UP COLORS
colorama.init(autoreset=True, convert=True)

# colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
white = Fore.WHITE
purple = Fore.LIGHTMAGENTA_EX
# dark color
gray = Fore.LIGHTBLACK_EX
black = Fore.LIGHTBLACK_EX


# version
version = '1.0'

def banner():
    # clear term for linux / windows
    system('cls;clear')

    print(f"""
            {purple}┌─────────────────────────────────────────────┐
            {purple}│                {white}Rx leaker                    {purple}│   {gray}- {black}github.com/{black}BlackRabbit-0{white}
            {purple}│                 {blue}────────{white}                  {purple}  │
            {purple}│           {gray}► {white}Version {yellow}{version}{white}         {purple}            │
            {purple}│           {gray}► {white}Backend {yellow}leaker{white}       {purple}           │
            {purple}└─────────────────────────────────────────────┘\n
                \n
    """)
