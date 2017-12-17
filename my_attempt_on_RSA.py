import random
from Crypto.Util.number import isPrime
from rsa.prime import gcd
from random import randint


def coprime(a,b):
    return gcd(a,b) == 1


def encrypt(message,e,n):
    i = 0
    msg = 1
    while i<e:
        msg *= message
        msg = msg%n
        i = i +1
    return msg


def decrypt(message,d,n):
    i=0
    msg=1
    while i<d:
        msg *= message
        msg = msg%n
        i = i +1
    return msg


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0


minPrime = 0
maxPrime = 25000
prime_numbers = [i for i in range(minPrime,maxPrime) if isPrime(i)]

p = random.choice(prime_numbers)

q = random.choice(prime_numbers)

n = p*q

phi_n = (p-1)*(q-1)

print("n: %d\n" % n)

e = randint(2,phi_n-1)
while not coprime(phi_n, e):
    e=randint(2,phi_n-1)

print("e: %d\n" % e)

b,x0,y0 = xgcd(phi_n,e)

d=y0

print("d: %d\n" % d)

print("phi(n): %d\n" % phi_n)

m = 500

encrypted = encrypt(m,e,n)

decrypted = decrypt(encrypted,d,n)

print("Message was %d\nEncrypted was %d, Decrypted was %d\n" % (m,encrypted,decrypted))





