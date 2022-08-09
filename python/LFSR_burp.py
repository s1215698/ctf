from Crypto.Util.number import*

def lfsr(R,mask):
    output = (R << 1) & 0xffffff    #将R向左移动1位，bin(0xffffff)='0b111111111111111111111111'=0xffffff的二进制补码
    i=(R&mask)&0xffffff             #按位与运算符&：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    lastbit=0
    while i!=0:
        lastbit^=(i&1)    #按位异或运算符：当两对应的二进位相异时，结果为1
        i=i>>1
    output^=lastbit
    return (output,lastbit)


bin_out = open('C:\ctf_share\e05281b9394c4032b443f9793b76be2a\key','rb').read()
key = []

for i in range(len(bin_out)):
    key.append(bin_out[i])
 
mask    =   0b1010011000100011100


for x in range(2**19):   #因題目 flag內19bits  所以用2**19  視題目提供
    judge=1
    R=x
    for i in range(12):                 #26-30行 視題目提供
        tmp=0
        for j in range(8):
            (x,out)=lfsr(x,mask)
            tmp=(tmp << 1)^out
        if(tmp!=key[i]):
            judge = 0
            break
    if(judge==1):
        print("flag{" + bin(R)[2:] + "}")
        break
        






