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

    print(f"""{black}Hello {green}Admin {black}| {purple}Discord: {white}Leon $#9346 {black}| {cyan}Instagram: {white}@xBackend {black}| {red}Telegram: {white}@xBackend  {black}| {red}New {yellow}Fresh {gray}V1 {cyan}Update {purple}Out!

                            {yellow}            ______              _                     _ 
                            {yellow}           (____  \            | |                   | |
                            {yellow}      _   _ ____)  )_____  ____| |  _ _____ ____   __| |
                            {yellow}     ( \ / )  __  ((____ |/ ___) |_/ ) ___ |  _ \ / _  |
                            {yellow}      ) X (| |__)  ) ___ ( (___|  _ (| ____| | | ( (_| |
                            {yellow}     (_/ \_)______/\_____|\____)_| \_)_____)_| |_|\____|
                                                                                          

                                         {white}╔════════════════{yellow}═══════════════════
                                         {white}║                                   
                                         {white}║    {yellow}User {gray}► {red}Admin                               
                                         {white}║    {yellow}Plan {gray}► {red}Owner                               
                                         {white}║                                   
                                         {white}╚════════════════{yellow}═══════════════════

                                         {white}╔════════════════{yellow}═══════════════════
                                         {white}║                                   
                                         {white}║    {yellow}Expiry {gray}► {red}106751.99                               
                                         {white}║    {cyan}VIP {gray}► {green}True    
                                         {white}║                                                              
                                         {white}╚════════════════{yellow}═══════════════════                                  \n
                \n
    """)
