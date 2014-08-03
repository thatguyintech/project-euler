'''
QUESTION:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

CORRECT ANSWER:

6857

'''

# pick a prime number, try dividing 600.. by that number, up to the square root (rounded down) of 600...

from math import sqrt

def isprime(n):
    limit = sqrt(n)
    x = 2 
    while x < limit:
        if n%x == 0:
            print n
            print x
            return False
        x += 1 
    return True

def sieve(n):
    check = [x for x in range(2, n)]
    for p in check:
        x = 1
        while x*p < n:
            if x*p in check:
                check.remove(x*p)
            x += 1
    if len(check) > 0:
        return check[-1]
    else:
        return False

def largest_prime(n):
    x = 1
    largest_prime_factor = 0

    while x < sqrt(600851475143):
        if isprime(x):
           if 600851475143 % x == 0:
                largest_prime_factor = x
        x += 1

    return largest_prime_factor
