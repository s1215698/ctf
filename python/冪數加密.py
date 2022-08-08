#coding=utf-8
#以下情形可考慮使用
#冪數加密



from posixpath import split
from struct import pack
import gmpy2
import libnum
from Crypto.Util.number import *
import rsa





def main():
    flag = "flag{1010101010101010101}"
    
    lib = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', 
           '10':'j', '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r',
           '19':'s', '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z'};
    
    
    input = '8842101220480224404014224202480122'
    #num = int(input)
    
    temp = input.split('0')
    
    s = ""
    var = []
    
    for x in range(0,len(temp)):
        s = ""
        num = int(temp[x])
        #print (num)
        while(num>0):
            s += str(num%10)
            num=num//10
        var += list(reversed(s))
        var += " "
          
    #print (var)
    
    result = []
    
    sum = 0
    for x in range(0,len(var)):
        
        if(var[x] == ' '):      
            result.append(str(sum))
            sum = 0
           
        elif(var[x]!=' '):
            tmp_num =  int(var[x])
            sum += tmp_num
            
            
    ans = ""
    for i in range(0,len(result)):
        ans += (lib.get(result[i]))
           
            
    print (ans)
                    
    

        
if __name__ == "__main__":
    main()