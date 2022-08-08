#coding=utf-8
#以下情形可考慮使用
#########1.提供一個密文和公鑰檔案
#2.透過openssl rsa -pubin -in [公鑰檔] -text -mudulus -noout 查得 n 和加密參數e
#3.n先轉成10進位 去http://factordb.com/ 利用n取p q值
#4.去算私鑰



from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa




n=87924348264132406875276140514499937145050893665602592992418171647042491658461
e=65537 

p=275127860351348928173285174381581152299
q=319576316814478949870590164193048041239

d=int(gmpy2.invert(e,(p-1)*(q-1)))


privatekey = rsa.PrivateKey(n , e , d , p , q)
with open("C:\ctf_share\\abc\\flag.enc","rb") as f:
    print(rsa.decrypt(f.read(),privatekey).decode())






'''
file = open("C:\\fllllllag.txt","rb")
c = int.from_bytes(file.read(),byteorder='big')
m= long_to_bytes(pow(c,d,n))
print (m)
'''