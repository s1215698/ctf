#coding=utf-8
#需用python2.7
#以下情形可考慮使用



from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa


x1 = "0xd5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed59"
x2 = "0x1338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3"
x3 = "0xd5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431"

#將x1-x3 轉成十進位
x1 = int(x1, 16)
x2 = int(x2, 16)
x3 = int(x3, 16)


def genKey(x1, x2):
    e = 65537
    N1 = e * x1 - 1
    N2 = e * x2 - 1

   # print(N1)
    for r in range(e):
        if N1 % (e - r) == 0:
            p = int(N1 // (e - r) + 1)
            if isPrime(p) == 1:
                print("r1=", r)
                break
    for r in range(e):
        if N2 % (e - r) == 0:
            q = int(N2 // (e - r) + 1)
            if isPrime(q):
                print("r2=", r)
                break
    n = p * q
    phi = (p - 1) * (q - 1)
    d = int(gmpy2.invert(e, phi))

    privatekey = rsa.PrivateKey(n, e, d, p, q)

    with open('C:/ctf_share/0803001/flag.enc', 'rb') as file:
        print(rsa.decrypt(file.read(), privatekey).decode())


genKey(x1, x2)