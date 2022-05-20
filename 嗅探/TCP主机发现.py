from scapy.all import *

ip = '127.0.0.1'
pkt = IP()/TCP()/b'hello world'
pkt[IP].dst = ip
pkt[TCP].flags = 'A'
result = sr1(pkt, timeout=1, verbose=False)
if result:
    result.display()
else:
    pass