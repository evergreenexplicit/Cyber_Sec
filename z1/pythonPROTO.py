from scapy.all import *
import sys
protos = []
methods=['GET','POST','HEAD','PUT','DELETE','CONNECT','OPTIONS','TRACE']#Define http methods
counter={}
protos.append('http')
counter['http'] = 0
httpsSites = []
packets = rdpcap(sys.argv[1])
for packet in packets:
    protName = packet.lastlayer().name
    if protName not in protos:
        counter[protName] = 0
        protos.append(protName)
    counter[protName] += 1
    if packet.haslayer(TCP):#Checks for TCP protocol
        if packet.dport == 80:#Checks for http port 80
          if packet.haslayer(Raw):#Checks if packet has payload
             r=packet[0][Raw].load
             for i in methods:
                    if i in str(r):
                        if(str(r)[:100] not in httpsSites):
                            httpsSites.append(str(r)[:100])
                        counter['http']+=1
                        
for proto in protos:
    print((proto + " " +str(counter[proto])))

for s in httpsSites:
    print(s)



'''
def ip_proto(pkt):
    global counter
    if hasattr(pkt,'proto'):
        proto_field = pkt.get_field('proto')
        return proto_field.i2s[pkt.proto]+"xd"
    elif hasattr(pkt,'type'):
        return str(pkt.type)+"xdd"
    elif hasattr(pkt,'nh'):
        return str(pkt.nh)+"xddd"
    else:
        counter+=1
        return "none"
'''