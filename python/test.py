#coding='utf-8'

import base64


cipher = input("輸入base64密文:\n")



print ("\n解密後為:\n"+base64.b64decode(cipher).hex())
