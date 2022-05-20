from scapy.all import *

def print_info(res):
    print('{}===>{}'.format(res[IP].src, res[IP].dst))

pkt = sniff(filter='host 192.168.30.211 && port 80', prn=print_info, count=5)
wrpcap('./http.pcap', pkt)