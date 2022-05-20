from scapy.all import *
ip : '127.0.0.1'
pkt = Ether()/ARP(dest=ip)
result = srp(pkt, timeout=1, verbose=False)
ans = result[0].res
num = len(ans)
for i in range(num):
    ip = ans[i][1][1].fields['psrc']
    mac = ans[i][1][1].fields['hwsrc']
    print("[+] %s  %s is up".format(ip, mac))