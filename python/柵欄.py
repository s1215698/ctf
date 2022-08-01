def generate_w(string, n): 
    '''將字符排列成w型'''
    array = [['.']*len(string) for i in range(n)] #生成初始矩陣
    row = 0
    upflag = False
    for col in range(len(string)): #在矩陣上按w型畫出string
        array[row][col] = string[col]
        if row == n-1:
            upflag = True
        if row == 0:
            upflag = False
        if upflag:
            row -= 1
        else:
            row += 1
    return array

def encode(string, n):
    '''加密'''
    array = generate_w(string, n)
    msg = []
    for row in range(n): #將每行的字符連起來
        for col in range(len(string)):
            if array[row][col] != '.':
                msg.append(array[row][col])
    return array, msg

def decode(string, n):
    '''解密'''
    array = generate_w(string, n)
    sub = 0
    for row in range(n): #將w型字符按行的順序依次替換為string
        for col in range(len(string)):
            if array[row][col] != '.':
                array[row][col] = string[sub]
                sub += 1
    msg = []
    for col in range(len(string)): #以列的順序依次連接各字符
        for row in range(n):
            if array[row][col] != '.':
                msg.append(array[row][col])
    return array, msg

def crack_cipher(string):
    '''破解密碼'''
    for n in range(2,len(string)): #遍歷所有可能的欄數
        print(str(n)+'欄：'+''.join(decode(string, n)[1]))

if __name__ == "__main__":
    string = "ccehgyaefnpeoobe{lcirg}epriec_ora_g"
    n = 5 #欄數

    #若不知道欄數，則遍歷所有可能
    crack_cipher(string)

    #若知道欄數
    #array,msg = decode(string, n)
    #array,msg = encode(string, n)
    for i in array: print(i)
    print(''.join(msg))