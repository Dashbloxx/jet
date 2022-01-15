import sys
import urllib.request
import json

# jet is a python script that uses all sorts of
# different APIs to get information of someone
# by simply using an IP address
# 
# !!	USE AT YOUR OWN RISK, THE CREATORS OF	!!
# !!	THIS SCRIPT ARE NOT RESPONSIBLE FOR	!!
# !!	YOUR ACTIONS USING THIS PYTHON SCRIPT	!!

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def sm(txt):
	print(bcolors.OKCYAN + "[" + bcolors.OKGREEN + "JET" + bcolors.OKCYAN + "]" + bcolors.OKBLUE + ": " + bcolors.HEADER + txt)
def sl(txt):
	print(bcolors.OKCYAN + "[" + bcolors.WARNING + "+" + bcolors.OKCYAN + "]" + bcolors.HEADER + txt)

if(len(sys.argv) == 1):
	sm("Error:\t" + bcolors.FAIL + "You haven't specified any arguments!")
	sm("Usage:\t" + bcolors.WARNING + "python3 jet.py <ip-address>")
elif(len(sys.argv) > 2):
	sm("Error:\t" + bcolors.FAIL + "You have specified way too many arguments!")
	sm("Usage:\t" + bcolors.WARNING + "python3 jet.py <ip-address>")
else:
	ipinfodata = json.loads(urllib.request.urlopen("https://ipinfo.io/" + sys.argv[1] + "/json").read())
	
	try:
		city = ipinfodata["city"]
	except:
		city = "UNKNOWN"
	try:
		region = ipinfodata["region"]
	except:
		region = "UNKNOWN"
	try:
		country = ipinfodata["country"]
	except:
		country = "UNKNOWN"
	try:
		coordinates = ipinfodata["loc"]
	except:
		coordinates = "UNKNOWN"
	try:
		postal = ipinfodata["postal"]
	except:
		postal = "UNKNOWN"
	try:
		timezone = ipinfodata["timezone"]
	except:
		timezone = "UNKNOWN"
	try:
		hostname = ipinfodata["hostname"]
	except:
		hostname = "UNKNOWN"
	try:
		org = ipinfodata["org"]
	except:
		org = "UNKNOWN"
	
	sl("\tCITY\t\t\t" + city)
	sl("\tREGION\t\t\t" + region)
	sl("\tCOUNTRY\t\t\t" + country)
	sl("\tCOORDINATES\t\t" + coordinates)
	sl("\tPOSTAL\t\t\t" + postal)
	sl("\tTIMEZONE\t\t" + timezone)
	sl("\tHOSTNAME\t\t" + hostname)
	sl("\tORGANIZATION\t\t" + org)