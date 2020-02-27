import requests
import os
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = ""
while True:
    cmd = raw_input("> ")
    r = requests.post(url, data={...})
    soup = BeautifulSoup(r.text, 'html.parser')
    out = soup.find('div')
    print out
