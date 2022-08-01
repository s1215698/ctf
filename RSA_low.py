#coding=utf-8
#需用python2.7
#以下情形可考慮使用
#1.加密指數e非常小
#2.一份明文使用不同的模數n，相同的加密指數e進行多次加密
#3.可以拿到每一份加密後的密文和對應的模數n、加密指數e

import json
import struct
import gmpy2


file = open("C:\ctf_share\enc.txt","r")
data = json.load(file)
def attack(list):
    def extended_gcd(a, b):
        x, y = 0, 1
        lastx, lasty = 1, 0
        while b:
            a, (q, b) = b, divmod(a, b)
            x, lastx = lastx - q * x, x
            y, lasty = lasty - q * y, y
        return (lastx, lasty, a)
    def CRT(items):
        N = 1
        for a, n in items:
            N *= n
        result = 0
        for a, n in items:
            m = N / n
            r, s, d = extended_gcd(n, m)
            if d != 1:
                N = N / n
                continue
            result += a*s*m
        return result % N, N
    x, n = CRT(list)
    m = gmpy2.iroot(x, 10)[0]
    return m

def long_to_bytes(n, blocksize=0):
    """Convert a positive integer to a byte string using big endian encoding.

    If :data:`blocksize` is absent or zero, the byte string will
    be of minimal length.

    Otherwise, the length of the byte string is guaranteed to be a multiple
    of :data:`blocksize`. If necessary, zeroes (``\\x00``) are added at the left.

    .. note::
        In Python 3, if you are sure that :data:`n` can fit into
        :data:`blocksize` bytes, you can simply use the native method instead::

            >>> n.to_bytes(blocksize, 'big')

        For instance::

            >>> n = 80
            >>> n.to_bytes(2, 'big')
            b'\\x00P'

        However, and unlike this ``long_to_bytes()`` function,
        an ``OverflowError`` exception is raised if :data:`n` does not fit.
    """

    if n < 0 or blocksize < 0:
        raise ValueError("Values must be non-negative")

    result = []
    pack = struct.pack

    # Fill the first block independently from the value of n
    bsr = blocksize
    while bsr >= 8:
        result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
        n = n >> 64
        bsr -= 8

    while bsr >= 4:
        result.insert(0, pack('>I', n & 0xFFFFFFFF))
        n = n >> 32
        bsr -= 4

    while bsr > 0:
        result.insert(0, pack('>B', n & 0xFF))
        n = n >> 8
        bsr -= 1

    if n == 0:
        if len(result) == 0:
            bresult = b'\x00'
        else:
            bresult = b''.join(result)
    else:
        # The encoded number exceeds the block size
        while n > 0:
            result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
            n = n >> 64
        result[0] = result[0].lstrip(b'\x00')
        bresult = b''.join(result)
        # bresult has minimum length here
        if blocksize > 0:
            target_len = ((len(bresult) - 1) // blocksize + 1) * blocksize
            bresult = b'\x00' * (target_len - len(bresult)) + bresult

    return bresult


list = []
for i in data:
    c = i['c']
    n = i['n']
    list.append((c, n))


print (long_to_bytes(attack(list)))

