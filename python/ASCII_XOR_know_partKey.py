from itertools import cycle
from operator import xor
from Crypto.Util.number import *

with open("C:/Users/ChingSi/Downloads/encrypted", "r" ) as f:
    raw = raw = f.read()

key_part = "XORISC"
out = open("C:/Users/ChingSi/Downloads/output.txt", 'w')
for i in range (32,127):
    for j in range (32,127):
        for k in range (32,127):
            key = key_part + chr(i) + chr(j) + chr(k)
            out.write ("key = " + key + ",")
            out.write ("flag = " + bytes([ord(i) ^ ord(j) for i, j in zip(raw, cycle(key))]).decode() + "\n")

out.close()
f.close()
'''
ans = bytes([ord(i) ^ ord(j) for i, j in zip(raw, cycle("XORISCOOL"))]).decode()

print (ans)
'''
#print (bytearray.fromhex(inp).decode())