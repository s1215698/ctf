from collections import Counter

enc = ['a','a','b','c','e','y','a','x','x']
enc_slice = enc[0::9]
print(Counter(enc_slice).most_common())