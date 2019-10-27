from subprocess import check_output
from scapy.all import *
import sys
command = ['geoiplookup']
packets = rdpcap(sys.argv[1])
counter = {}
countries = []
destinations = []
for p in packets:
    if p.haslayer(IP):
        dest = p.getlayer(1).dst
        if dest not in destinations: 
          destinations.append(dest)
          c = check_output(command + [dest])
          if c not in countries:
              countries.append(c)
              counter[c] = 0
          counter[c]+=1


for c in countries:
    print((str(c)[25:-3] + " Number of packets:" + str(counter[c])))
              