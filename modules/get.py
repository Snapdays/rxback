from ctypes import wstring_at
import requests, socket, subprocess, shodan
from urllib.parse import urlparse
from shodan import Shodan
from bs4 import BeautifulSoup
from modules.banner import *
from modules.dns import DNSDumpsterAPI

timeouts = 5


def testconnect(url):
    try:
        # get website status code and test local connection
        testconnect = requests.get(url, timeout=5).status_code

        if testconnect == 301:
            print(f"    {red}Error {gray}► {white}looks like {url} is giving us a {red}{testconnect}{white} statuscode")
            exit(0)

        # testconnect == 403:
        #  print(
        #     f"      {red}Error {gray}► {white}looks like {url} is giving us a {red}{testconnect}{white} statuscode")
        # exit(0)

        return

    # connection timeout
    except requests.exceptions.Timeout:
        print(f"      {red}Error {gray}► {white}looks like {yellow}{url}{white} has timeout")
        exit(0)

    # connection refused
    except requests.exceptions.ConnectionError:
        print(f"      {red}Error {gray}► {white}looks like {yellow}{url}{white} could not connect")
        exit(0)


def mailman(url):
    # from the creator of this exploit, i am always looking for new ways
    try:
        check = requests.get(url + "//mailman/listinfo/mailman", timeout=timeouts)
        if check.status_code == 404:
            return {
                "backend": False
            }
        try:
            soup = subprocess.getoutput(f"curl {check.url} -s | findstr POST").split('"')[1].replace(
                '/mailman/listinfo/mailman', '')

            return {
                "backend": soup
            }
        except:
            return {
                "backend": False
            }

    except requests.exceptions.Timeout:
        return {
            "backend": False
        }


def GetDomainIP(url):
    # domain to ip
    domain = urlparse(url).netloc
    try:

        return {
            # connect to domain and grab host
            "ip": socket.gethostbyname(domain),
            "cf": f"{white}Cloudflare"
        }
    except:
        return "None"


def cpanel(url):
    try:
        cpan = requests.get(url + "//cpanel", timeout=timeouts, allow_redirects=False)
        if cpan.status_code == 404:
            return {
                "cpanel": False
            }
        if "cpanel" in cpan.text:
            pass
        else:
            return {
                "cpanel": False
            }

        connect = cpan.url.replace('/cpanel', '').replace('/', '').replace('http:', '').replace('https:', '')
        try:
            ui = requests.get("https://" + connect + ":2083")

        except requests.exceptions.ConnectionError:
            return {
                "cpanel": False
            }
        lol = cpan.url.replace('/cpanel', '').replace('/', '').replace('http:', '').replace('https:', '')

        return {
            "cpanel": lol + ":2083"

        }
    except:
        return {
            "cpanel": False
        }


def redd(url):
    # catches redu
    try:
        head = requests.get(url, timeout=timeouts, allow_redirects=False).headers
        try:
            return {
                "red": head['location'],
            }
        except:
            return {
                "red": False
            }
    except requests.exceptions.Timeout:
        pass


def total(url):

    oop = url.replace('https:', '').replace('/', '').replace('http:', '').replace('//', '')
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey': "3efa6fc22eb53ade73ed29357896233fb1007d40c354afe0451a607f7157f64b", 'domain': oop}

    response = requests.get(url, params=params)
    jdata = response.json()

    domains = sorted(jdata['subdomains'])
    try:
        io = jdata['undetected_referrer_samples'][1]['date']
    except:
        io = ""
        pass
    # print(jdata)
    for domain in domains:
        try:

            lol = socket.gethostbyname(domain)
        except:
            lol = f"{red}None"
            pass



        try:
            stat = False

            if "172." in lol or "8." in lol or "103." in lol or "104." in lol or "23." in lol or "173." in lol:
                if "104" in lol:
                    stat = True
                stat = True

            if len(io) == 0:
                io = f"{red}None"


            req = requests.get(f"https://{lol}/", timeout=10)
            soup = BeautifulSoup(req.text, 'html.parser')
            print(stat)
            if stat == True:
                print(f"    {gray}► {white} Found " + domain, f"IP {gray}" + lol,
                      f"{white} Date: {yellow}" + io + f"{gray} (CloudFlare)")
            else:
                oo = 0
                for title in soup.find_all('title'):
                    oo = title.get_text()
                if len(oo) == 0:
                    print(f"    {gray}► {green} Found {white}" + domain, f"IP {yellow}" + lol, f"{white} Date: {yellow}" + io + f" {white}HeaderTitle: {gray}empty")
                else:
                    print(f"    {gray}► {green} Found {white}" + domain, f"IP {yellow}" + lol, f"{white} Date: {yellow}" + io + f" {white}HeaderTitle: {yellow}{oo}")
        except:
            print(f"    {gray}► {green} Found {white}" + domain, f"IP {yellow}" + lol,
                  f"{white} Date: {yellow}" + io + f" {white}HeaderTitle: {gray}empty")
            if "172." in lol or "8." in lol or "103." in lol or "104." in lol or "23." in lol or "173." in lol:

                print(f"    {gray}► {green} Found {white}" + domain, f"IP {yellow}" + lol,
                      f"{white} Date: {yellow}" + io + f" {white}HeaderTitle: {gray}empty (CloudFlare)")






def sho(url):
    REQ_URL = url.replace('https:', '').replace('/', '').replace('http:', '').replace('//', '')
    try:
        API = Shodan("eutNHipEhVtJhBIGdzltWKOgOKOOmxJ6")
        results = API.search(REQ_URL)
        for result in results['matches']:
            return {
                "shodan": result['ip_str'],
                "res": result['domains']
            }
    except:
        return {
            "shodan": False
        }


def hackertarget(url):
    data = {
        "theinput": url,
        "thetest": "dnslookup",
        "name_of_nonce_field": "8ea1835740",
        "_wp_http_referer": "%2Fdns-lookup%2F"
    }
    test = requests.post("https://hackertarget.com/dns-lookup/", data=data)
    soup = BeautifulSoup(test.text, 'html.parser')
    for txt in soup.find(id="formResponse"):
        print(txt)


def dnsdumpster(target):
    res = DNSDumpsterAPI(False).search(target)

    if res['dns_records']['host']:
        for entry in res['dns_records']['host']:
            provider = str(entry['domain'])
            if "cloudflare" not in provider or "ddos-guard" not in provider:
                lol = entry['ip']

                if "172." in lol or "103." in lol or "104." in lol or "23." in lol or "173." in lol:
                    print(f"    {gray}► {red}HOST: {white}{entry['domain']}{white} {gray}{entry['ip']} (CloudFlare)")
                else:
                    print(f"    {gray}► {red}HOST: {white}{entry['domain']}{white} {yellow}{entry['ip']}")
    else:
        print(f"    {gray}► {red}no host records found or they don't match {yellow}cloudflare or ddos-guard")

    if res['dns_records']['dns']:
        for entry in res['dns_records']['dns']:
            provider = str(entry['domain'])
            if "cloudflare" not in provider or "ddos-guard" not in provider:
                lol = entry['ip']
                if "172." in lol or "103." in lol or "104." in lol or "23." in lol or "173." in lol:
                    print(f"    {gray}► {green}Found DNS: {white}{entry['domain']} {gray}{entry['ip']} (CloudFlare)")
                else:
                    print(f"    {gray}► {green}Found DNS: {white}{entry['domain']} {yellow}{entry['ip']}")
    else:
        print(f"    {gray}► {red}no dns records found or they don't match {yellow}cloudflare or ddos-guard")

    if res['dns_records']['mx']:
        for entry in res['dns_records']['mx']:
            provider = str(entry['domain'])
            if "cloudflare" not in provider or "ddos-guard" not in provider:
                lol = entry['ip']
                if "172." in lol or "103." in lol or "104." in lol or "23." in lol or "173." in lol:
                    print(f"    {gray}► {green}Found MX: {white}{entry['domain']} {gray}{entry['ip']} (CloudFlare)")
                else:
                    print(f"    {gray}► {green}Found MX: {white}{entry['domain']} {yellow}{entry['ip']}")

    else:
        print(f"    {gray}► {red}no mx records found or they don't match {yellow}cloudflare or ddos-guard")
