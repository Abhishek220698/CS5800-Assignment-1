import random
from math import pow

a = random.randint(2, 10)

# To find gcd of two numbers
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# For key generation i.e. large random number
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

# For asymmetric encryption
def encryption(msg1, msg2, q, h, g):
    k1 = gen_key(q)
    k2 = gen_key(q)
    s1 = power(h, k1, q)
    s2 = power(h, k2, q)
    p1 = power(g, k1, q)
    p2 = power(g, k2, q)

    ct1 = [s1 * ord(m) for m in msg1]
    ct2 = [s2 * ord(m) for m in msg2]

    return (ct1, ct2, p1, p2)

# For decryption
def decryption(ct1, ct2, p1, p2, key, q):
    h1 = power(p1, key, q)
    h2 = power(p2, key, q)

    pt1 = [chr(int(c / h1)) for c in ct1]
    pt2 = [chr(int(c / h2)) for c in ct2]

    return ''.join(pt1), ''.join(pt2)

# Test the encryption and decryption functions
msg1 = input("Enter message 1: ")
msg2 = input("Enter message 2: ")
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)
h = power(g, key, q)

print("g used=", g)
print("g^a used=", h)

ct1, ct2, p1, p2 = encryption(msg1, msg2, q, h, g)

print("Original messages=", msg1, msg2)
print("Encrypted messages=", ct1, ct2)

pt1, pt2 = decryption(ct1, ct2, p1, p2, key, q)

print("Decrypted messages=", pt1, pt2)

