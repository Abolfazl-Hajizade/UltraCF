#!/usr/bin/python

import requests
import socket
from bs4 import BeautifulSoup
import re
from colorama import init,Fore,Back,Style

init(autoreset=True)                

fg = Fore.GREEN;fw = Fore.WHITE;fr = Fore.RED;fy = Fore.YELLOW
sn = Style.BRIGHT
G = fg + sn;W = fw + sn;R = fr + sn;Y = fy + sn
  
cloudflare_ip = ""
filter_1 = ""

def banner():

    print('''

            ooooo     ooo oooo      .                           .oooooo.   oooooooooooo
            `888'     `8' `888    .o8                          d8P'  `Y8b  `888'     `8
             888       8   888  .o888oo oooo d8b  .oooo.      888           888
             888       8   888    888   `888""8P `P  )88b     888           888oooo8
             888       8   888    888    888      .oP"888     888           888    "
             `88.    .8'   888    888 .  888     d8(  888     `88b    ooo   888
               `YbodP'    o888o   "888" d888b    `Y888""8o     `Y8bood8P'  o888oo


                 > Team : UltraSecurity 
                 > Programmer : abolfazl hajizade 
                 > Gmail: zeroday1010@gmail.com

    ''')

def check_cloudflare(website):

    print(Y+"\n[>] Check Cloudflare:\n"+W)

    pay = {"domain":website}

    url = "https://www.ultratools.com/tools/dnsLookupResult"

    try:

        r = requests.post(url,pay)

    except:
            print(R+"\n[!] Please Check Your Connection OR Target domain ex(website.com)\n"+W)
            exit()

    source = r.content

    if "cloudflare" in source:

            print(G+"\n[+] WebSite Using Cloudflare\n"+W)

            cloudflare_ip = socket.gethostbyname(website)

            filter_1 = cloudflare_ip.split(".")

            print("[+] Cloudflare ip : "+R+cloudflare_ip+W+"\n")
    else:
            print(R+"\n[X] WebSite Not Using Cloudflare\n"+W)
            exit()


def ip_history(website):

        print(Y+"[>] ip history:\n"+W)

        url = "https://viewdns.info/iphistory/?domain="+website

        r = requests.get(url)

        sourcce = r.content

        soup = BeautifulSoup(sourcce , "html.parser")

        res = soup.find("font" , face="Courier")

        ips = re.findall("(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",res.text)

        list_1 = []

        for i in ips:
                  
                if i in list_1:
                        
                        continue

                list_1.append(i)  
            
        cloudflare_ip = socket.gethostbyname(website)
        filter_1 = cloudflare_ip.split(".")
        
        for i in list_1:

            filter_2 = i.split(".")
            
            if filter_1[0] == filter_2[0]:
                
                    print("   "+R+i+"  CloudFlare"+W)
            else:
                    print("   "+G+i+W)
        
        print("\n\n")

def dns_brute(website):

        print (Y+"[>] DNS Bruting:\n"+W)
        dnslist = ["ftp", "cpanel", "webmail", "localhost", "local", "mysql", "forum", "driect-connect", "blog",
                         "vb", "forums", "home", "direct", "forums", "mail", "access", "admin", "administrator",
                         "email", "downloads", "ssh", "owa", "bbs", "webmin", "paralel", "parallels", "www0", "www",
                         "www1", "www2", "www3", "www4", "www5", "shop", "api", "blogs", "test", "mx1", "cdn", "mysql",
                         "mail1", "secure", "server", "ns1", "ns2", "smtp", "vpn", "m", "mail2", "postal", "support",
                         "web", "dev","dl","tools","news"]

        cloudflare_ip = socket.gethostbyname(website)
        filter_1 = cloudflare_ip.split(".")
        for dns in dnslist:
            try:
                    hosts = str(dns) + "." + str(website)
                    ip_ = socket.gethostbyname(str(hosts))
                    filter_2 = ip_.split(".")
                    if filter_1[0] == filter_2[0]:
                            print("[+] DNS => " +R+ip_+W+' | '+hosts)
                    else:
                            print("[+] DNS => " +G+ip_+W+' | '+hosts)
            except:
                    pass
        

if __name__ == "__main__":

    banner()
    website = raw_input("\n[>] Enter Website: ")
    if website == "":
        website = "ultrasec.org"
    try:
            socket.gethostbyname(website)
    except:
            print(R+"\n[!] Please Check Target Domain ...\n"+W)
            exit()
    check_cloudflare(website)
    ip_history(website)
    dns_brute(website)

    











