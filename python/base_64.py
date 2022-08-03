#coding='utf-8'
import base64
import sys

def main():
    #choose = input("目標:\n1、Base64加密\n2、Base64解密\n")

    #if choose == '1':
        #plain = input("輸入欲加密明文:\n")
        #print ("\n加密後為:\n" + base64.b64encode(plain)).
        #sys.exit()

    #elif choose == '2':
        cipher = input("輸入base64密文:\n") 
        print ("\n解密後為:\n"+ base64.b64decode(cipher).hex())
    
    #else :
        #print ("NO......")
        #sys.exit()

if __name__ == "__main__":
    main()

