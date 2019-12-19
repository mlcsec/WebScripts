import requests
import sys

if len(sys.argv) != 3:
    sys.exit("usage: python %s <url> <wordlist>" % sys.argv[0])

url = sys.argv[1]
wordlist = sys.argv[2]

if url.endswith("/"):
    pass
else:
    url = url+"/"

words = [line.strip('\n') for line in open(wordlist)]

for w in words:
    try:
        response = requests.get(url+w)
        if response.status_code == 200:
            print "[+] " + url+w + " 200 OK"
        if response.status_code == 403:
            print "[-] " + url+w + " 403 FORBIDDEN"
    except KeyboardInterrupt:
        sys.exit(0)
