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




n=66473473500165594946611690873482355823120606837537154371392262259669981906291
e=65537 

p=800644567978575682363895000391634967
q=83024947846700869393771322159348359271173

d=int(gmpy2.invert(e,(p-1)*(q-1)))


privatekey = rsa.PrivateKey(n , e , d , p , q)
with open("C:\ctf_share\\rsa\\flag.enc","rb") as f:
    print(rsa.decrypt(f.read(),privatekey).decode())






'''
file = open("C:\\fllllllag.txt","rb")
c = int.from_bytes(file.read(),byteorder='big')
m= long_to_bytes(pow(c,d,n))
print (m)
'''