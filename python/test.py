#coding=utf-8
#需用python2.7
#以下情形可考慮使用
#只給部分私鑰 ==> 利用RSA私鑰格式去反推



from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa





def main():
    flag = "flag{1010101010101010101}"
    
    R=int(flag[5:-1],2)
    print (R)
        
if __name__ == "__main__":
    main()