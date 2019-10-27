from scapy.all import *
import sys
devIPs = set()
packetsDNS = rdpcap(sys.argv[1])
for p in packetsDNS:
    if p.haslayer(DNS):
        devIPs.add(p.getlayer(1).src)
for ip in devIPs:
    print(ip)
