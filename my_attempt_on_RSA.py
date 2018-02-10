import timeit
from random import randint

from rsa.prime import gcd
from sympy import isprime


def coprime(a, b):
    return gcd(a, b) == 1


def encrypt(message, e, n):
    i = 0
    msg = 1
    while i < e:
        msg *= message
        msg = msg % n
        i = i + 1
    return msg


def decrypt(message, d, n):
    i = 0
    msg = 1
    while i < d:
        msg *= message
        msg = msg % n
        i = i + 1
    return msg


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2 ** (n - 1), 2 ** n)
        if isprime(p):
            return p


bits = 2048
start = timeit.default_timer()
p = generate_big_prime(bits)

q = generate_big_prime(bits)

n = p * q

phi_n = (p - 1) * (q - 1)

print("n: %d\n" % n)

print("phi(n): %d\n" % phi_n)

e = randint(2, phi_n - 1)
while not coprime(phi_n, e):
    e = randint(2, phi_n - 1)

print("e: %d\n" % e)

b, x0, y0 = xgcd(phi_n, e)

d = y0

print("d: %d\n" % d)

stop = timeit.default_timer()
print("Created RSA key within %f s" % (stop - start))

m = 500

start = timeit.default_timer()
encrypted = encrypt(m, e, n)
stop = timeit.default_timer()
print("Encrypted within %f s" % (stop - start))

start = timeit.default_timer()
decrypted = decrypt(encrypted, d, n)
stop = timeit.default_timer()
print("Decrypted within %f s" % (stop - start))

print("Message was %d\nEncrypted was %d, Decrypted was %d\n" % (m, encrypted, decrypted))
