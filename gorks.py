# implement https://github.com/s0md3v/goop
import sys
from time import sleep
from random import randint
from googlesearch import search
from argparse import ArgumentParser

parser = ArgumentParser()
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-d', dest="dom", help="domain")
args = parser.parse_args()
dom = args.dom

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

orParams = ['next=', 'url=', 'target=', 'rurl=', 'dest=', 'destination=', 'redir=', 'Url=', 'URL=', 'RedirectURL=', 'redirectUrl=', 'redirect_uri=', 'redirect_url=', 'redirect=', 'redirect/', '/cgi-bin/redirect.cgi?', '/out/', '/out?', 'view=', '/login?to=', 'image_url=', 'go=', 'return=', 'returnTo=', 'return_to=', 'checkout_url=', 'continue=', 'return_path=']

for i in orParams:
    query = "inurl:%s site:%s" % (i, dom)
    print ("[+] Google: " + query)
    for s in search(query, tld="com", num=10, stop=50, pause=5):
        #print "[+] " + query
        print(s)
        #sleep(randint(10,100))


#query = "inurl:next= OR inurl:url= OR inurl:target= OR inurl:rurl= OR inurl:dest= OR inurl:destination= OR inurl:redir= OR inurl:Url= OR inurl:URL= OR inurl:RedirectURL= OR inurl:redirectUrl= OR inurl:redirect_uri= OR inurl:redirect_url= OR inurl:redirect= OR inurl:redirect/ OR inurl:/cgi-bin/redirect.cgi? OR inurl:/out/ OR inurl:/out? OR inurl:view= OR inurl:/login?to= OR inurl:image_url= OR inurl:go= OR inurl:return= OR inurl:returnTo= OR inurl:return_to= OR inurl:checkout_url= OR inurl:continue= OR inurl:return_path= site:%s" % (dom)
