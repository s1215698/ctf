#coding=utf-8
#需用python2.7
#以下情形可考慮使用
#1.已知p,q,e(public key),c
#2.可計算得d(private key),n


import gmpy2
import libnum
from Crypto.Util.number import *
import rsa



p=hex(275127860351348928173285174381581152299)
q=hex(319576316814478949870590164193048041239)
n=p*q



e=hex(65537)
c=0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520

d=gmpy2.invert(e,(p-1)*(q-1))

m=long_to_bytes(pow(c,d,n))

print (d)
