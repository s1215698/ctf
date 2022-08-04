#coding=utf-8
#以下情形可考慮使用




from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa



##rb  r  

def main():
    file = open("C:\ctf_share\\0803002\key","rb") 
    content = file.read()
    list = []
    for i in content:
        list.append(i)
        
        
    print (list)
        
if __name__ == "__main__":
    main()