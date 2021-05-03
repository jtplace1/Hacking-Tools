from scapy.all import *
from scapy.layers.inet import ICMP

conf.verb = 0

f = open('C:/Documents/test.txt')
data = f.read()
f.close()
host =  "127.0.0.1"

print(" Data size is %d " % len(data))

i =0
while i < len(data):
    pack = IP(dst=host)/ICMP(type="echo-reply")/data[i:i+32]
    send(pack)
    i=i+32
print ("Data sent")
