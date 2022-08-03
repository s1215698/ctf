#coding=utf-8
#以下情形可考慮使用
#1.提供一個密文和公鑰檔案
#2.透過openssl rsa -pubin -in [公鑰檔] -text -mudulus -noout 查得 n 和加密參數e
#3.n先轉成10進位 去http://factordb.com/ 利用n取p q值
#4.去算私鑰



from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa




n=76775333340223961139427050707840417811156978085146970312315886671546666259161
e=65537 

p=273821108020968288372911424519201044333
q=280385007186315115828483000867559983517

d=int(gmpy2.invert(e,(p-1)*(q-1)))


privatekey = rsa.PrivateKey(n , e , d , p , q)
with open("C:\\fllllllag.txt","rb") as f:
    print(rsa.decrypt(f.read(),privatekey).decode())






'''
file = open("C:\\fllllllag.txt","rb")
c = int.from_bytes(file.read(),byteorder='big')
m= long_to_bytes(pow(c,d,n))
print (m)
'''