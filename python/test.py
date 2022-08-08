# Embedded file name: ans.py
import base64

def encode1(ans):
    s = ''
    for i in ans:
        x = ord(i) ^ 36
        x = x + 25
        s += chr(x)

    return s

def decode1(ans):
    s = ''
    for i in ans:
        x = ord(i) - 25
        x = x ^ 36
        
        s += chr(x)

    return s


def encode2(ans):
    s = ''
    for i in ans:
        x = ord(i) + 36
        x = x ^ 36
        s += chr(x)

    return s

def decode2(ans):
    s = ''
    for i in ans:
        
        x = i ^ 36
        x = x - 36
        s += chr(x)

    return s


def encode3(ans):
    return base64.b32encode(ans)



final = 'UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==='

    
    
    
final = base64.b32decode(final)
final = decode2(final)
final = decode1(final)
    
print(final)
    