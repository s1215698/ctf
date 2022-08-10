with open("C:\ctf_share\\0810001\qexmry7.txt", "r") as f:
    raw = f.read()
enc = bytes.fromhex(raw)
'''
print("First 25 decoded", enc[:25])
print("enc length:", len(enc))
print(
    "Min:", min(enc),
    "Max:", max(enc),
    "Unique:", len(set(enc))
)
'''

#嘗試key長度
from string import printable
printable_set = set(printable.encode())

for key in range(128):
    pln = bytes([i ^ key for i in enc])
    if all([i in printable_set for i in pln]):
        print("Found key:", key)
        
for key_len in range(1, 50):
    print("Try key length", key_len)
    all_key_pos_valid = True
    for key_pos in range(key_len):
        print("Position", key_pos, ": ", end="")
        enc_slice = enc[key_pos::key_len]
        key_pos_valid = False
        for key in range(128):
            pln_slice = [i ^ key for i in enc_slice]
            if all([i in printable_set for i in pln_slice]):
                key_pos_valid = True
                print(f"{key} ", end="")
        print()
        if not key_pos_valid:
            all_key_pos_valid = False
    if all_key_pos_valid:
        print("Key length", key_len, "is possible")
        break
    print()
   
from collections import Counter

#range帶入key長度
space_key = []
e_key = []
t_key = []
for key_pos in range(33):
    enc_slice = enc[key_pos::key_len]
    most_common_enc = Counter(enc_slice).most_common(1)[0][0]
    space_key.append(most_common_enc ^ ord(" "))
    e_key.append(most_common_enc ^ ord("e"))
    #t_key.append(most_common_enc ^ ord("t"))
print("Space key:", bytes(space_key).decode())
#print("e key    :", bytes(e_key).decode())
#print("t key    :", bytes(t_key).decode())





#用key解密
from itertools import cycle

pln = bytes([
    i ^ j
    for i, j in zip(enc, cycle(b"We finish each other's Sandwiches"))
]).decode()


#print(pln)