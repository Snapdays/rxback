# /* backend leaker */
# /* made by nano */ - cybersecurity at it's finest

from time import sleep
from time import process_time
from modules.banner import *
from modules.dns import *
from modules.get import *
import shodan
import ctypes


def handleurl():
    ctypes.windll.kernel32.SetConsoleTitleW("[ rx leaker ] - Waiting for target")

    url = input(f"      {white}Url {gray}►{white} ")

    # url handling
    if "https" in url or "http" in url:
        pass
    else:
        url = "https://" + url

    # testing url
    ctypes.windll.kernel32.SetConsoleTitleW(f"[ rx leaker ] - testing {url} connection")
    # connection speed
    t1_start = process_time()
    testconnect(url)
    t1_stop = process_time()
    sleep(3)
    print(f"      {white}Url {gray}► {green}ONLINE{white}")
    sleep(2)
    print(f"      Status {gray}► {green}200")
    print(f"      Speed {gray}► {yellow}{t1_stop - t1_start}")
    sleep(4)
    system('cls;clear')
    banner()
    ctypes.windll.kernel32.SetConsoleTitleW(f"[ rx leaker ] - Scanning {url}")

    print(f"    {gray}► {white}Starting backend enum...\n")
    rawip = GetDomainIP(url)

    # check ip ranges if cloudflare
    if "172." in rawip['ip'] or "103." in rawip['ip'] or "108." in rawip['ip'] or "104." in rawip['ip']:
        print(f"    {gray}► {white}RAW IP {yellow}{rawip['ip']} {rawip['cf']}")
    else:
        print(f"    {gray}► {white}RAW IP {yellow}{rawip['ip']}")
    # headers
    head = redd(url)
    if not head['red']:
        print(f"    {gray}► {white}redirects = {yellow}False")
    else:
        print(f"    {gray}► {white}redirect {green}{head['red']}")
    # backend / leakage
    mail = mailman(url)
    if not mail['backend']:
        print(f"    {gray}► {white}SMP backend {yellow}not found")
    else:
        print(f"    {gray}► {white}FOUND SMP backend {green}{mail['backend']}")
        io = GetDomainIP(mail['backend'])
        print(f"    {gray}► {white}FOUND SMP IP {green}{io['ip']}")
    # uses the cpanel module
    cpan = cpanel(url)
    if not cpan['cpanel']:
        print(f"    {gray}► {white}cpanel {yellow}not found")
    else:
        print(f"    {gray}► {white}FOUND cpanel {green}{cpan['cpanel']}")
    # uses the DnsDumpster module
    print(f"\n    {gray}► {white}Scanning DnsRecords...\n")
    dump = urlparse(url).netloc
    dnsdumpster(dump)
    # uses the viurstotal module
    try:
        print(f"\n    {gray}► {white}Scanning Subdomains...\n")
        total(url)
    except Exception as e:
        print(f"    {gray}► {white}Could not find any subdomains")

        pass
    print(f"\n    {gray}► {white}Scanning Shodan...\n")
    # shodan module
    shodan = sho(url)
    try:
        if not shodan['shodan']:
            print(f"    {gray}► {white}No results on shodan")
            pass
        else:
            print(f"    {gray}► {white}Found {shodan['res']} {shodan['shodan']}")

    except TypeError:
        print(f"    {gray}► {white}No results on shodan")
        pass





    # did not include hackertarget / formatting bad does not match rx theme
    # hackertarget(url)
    # choices
    print(f"\n    {gray}► {white}would u like to scan another target? (y/n) \n")
    option = input(f"    {gray}► {white}")
    if option == "y":
        banner()
        handleurl()
    elif option == "n":
        exit(0)
    else:
        banner()
        handleurl()

if __name__ == '__main__':
    banner()
    handleurl()
