#coding=utf-8
#轉10進制用int()   
#轉16進制用hex()
#(字串).encode("utf-8").hex()
#base64.b64decode(字串).hex()
import base64
import sys

s = "Os9mhOQRdqW2cwVrnNI72DLcAXoXUJ1HGwJBANWiJcDUGxZpnERxVw7s0913WXNtV4GqdxCzG0pG5EHThtoTRbyX0aqRP4U/hQ9tRoSoDmBn+3HPITsnbCy67vkCQBM4xZPTtUKM6Xi+16VTUnFVs9E4rqwIQCDAxn9UuVMBXlX2Cl0x0GUF4C5hItrX2woF7LVS5EizR63CyRcPovMCQQDVyNbcWD7N88MhZjujKuSrHJot7WcCaRmTGEIJ6TkU8NWt9BVjR4jvkZ2EqNd0KZWdQPukeynPcLlDEkIXyaQx"

print (base64.b64decode(s).hex())