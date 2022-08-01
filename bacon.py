import re


LETTERS = [
            'A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z'
]
CIPHER = [
            "aaaaa","aaaab","aaaba","aaabb","aabaa","aabab",
            "aabba","aabbb","abaaa","abaab","ababa","ababb",
            "abbaa","abbab","abbba","abbbb","baaaa","baaab",
            "baaba","baabb","babaa","babab","babba","babbb",
            "bbaaa","bbaab"
]



def bacon1(string):
    list = []
    #cut per 5 char
    for i in range(0,len(string),5):
        list.append(string[i:i+5])

    #print(list)
    #比對每組對應之字母,並以小寫呈現
    for i in range(0,len(list)):
        for j in range (0,26):
            if list[i] == CIPHER[j]:
                print(LETTERS[j].lower(),end="")
    print("")

def main():
    #密文放ciphertext
    ciphertext = "aaaaabaabbbaabbaaaaaaaabaababaaaaaaabbabaaabbaaabbaabaaaababaabaaabbabaaabaaabaababbaabbbabaaabababbaaabbabaaabaabaabaaaabbabbaabbaabaabaaabaabaabaababaabbabaaaabbabaabba"
    bacon1(ciphertext)
    
    

if __name__ == "__main__":
    main()