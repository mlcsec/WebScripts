# loop through supplied url list/wordlist
# use Go instead? 

import requests
import sys
from argparse import ArgumentParser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


parser = ArgumentParser()
requiredName = parser.add_argument_group('required arguments')
requiredName.add_argument('-u', dest="url", help="url")
#requiredName.add_argument('-w', dest="wordlist", help="wordlist")
args = parser.parse_args()
url = args.url

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

# Directory listing for
# Index of 
# To parent directory

req = requests.get(url)
data = req.content

if "Directory listing for" in str(data):
    print("[+] Directory listing found!")
    print("[+] URL: %s" % url)
    print("[+] Code: "+ str(req.status_code))
    print("[+] Length: "+ str(len(req.content)))
else:
    pass
