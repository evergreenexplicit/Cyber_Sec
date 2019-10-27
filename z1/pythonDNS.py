from scapy.all import *
import sys
names = []
DNSpackets = rdpcap(sys.argv[1])

for packet in DNSpackets:
    if packet.haslayer(DNS):
        queryName = packet.qd.qname
        if queryName not in names:
            names.append(queryName)


for q in names:
    print(q.decode())

