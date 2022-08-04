#coding=utf-8
#以下情形可考慮使用
######只給部分私鑰 ==> 利用RSA私鑰格式去反推



from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa





def genKey(x1, x2):
    e = 65537
    
    #N1,N2分別為r1(p-1)、r2(q-1)   r1 < e  r2 < e
    N1 = e * x1 - 1
    N2 = e * x2 - 1

   
    #嘗試所有r1 r2的值 分別可以整除N1和N2  p = N1//r1 +1  q = N2//r2+1
    for r1 in range(1,e):
        if N1 % r1 == 0:
            p = int(N1 // r1 + 1)
            if isPrime(p) == 1:
                print("r1=", r1)
                break
            
    for r2 in range(1,e):
        if N2 % r2 == 0:
            q = int(N2 // r2 + 1)
            if isPrime(q) == 1:
                print("r2=", r2)
                break
            
    n = p * q
    phi = (p - 1) * (q - 1)  #phi=尤拉函數
    d = int(gmpy2.invert(e, phi))

    privatekey = rsa.PrivateKey(n, e, d, p, q)

    with open('C:/ctf_share/0803001/flag.enc', 'rb') as file:
        print(rsa.decrypt(file.read(), privatekey).decode())

def main():
    x1 = "0xd5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed59"
    x2 = "0x1338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3"
    x3 = "0xd5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431"

    #將x1-x3 轉成十進位
    x1 = int(x1, 16)
    x2 = int(x2, 16)
    x3 = int(x3, 16)
    
    
    genKey(x1, x2)
    
if __name__ == "__main__":
    main()