#coding=utf-8
#需用python2.7
#以下情形可考慮使用
#1.有兩組C(密文) 兩組n 加密指數e相同
#2.利用兩個n求最大公因數得出p數值  ==>依序求出q值
#3.利用gmpy.invert 去求得私鑰
#4.用pow去求明文


from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa


n=76775333340223961139427050707840417811156978085146970312315886671546666259161
e=65537 


#http://factordb.com/ 利用n取pq值
p=273821108020968288372911424519201044333
q=280385007186315115828483000867559983517

d=gmpy2.invert(e,(p-1)*(q-1))

'''
file = open("C:\\fllllllag.txt","rb")
c = int.from_bytes(file.read(),byteorder='big')
m= long_to_bytes(pow(c,d,n))
print (m)
'''




privatekey = rsa.PrivateKey(n , e , d , p , q)
with open("C:\\fllllllag.txt","rb") as f:
    print(rsa.decrypt(f.read(),privatekey).decode())
    