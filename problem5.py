'''
QUESTION:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

CORRECT ANSWER:
232792560

'''
'''
1 2 3 4 5 6 7 8 9 10
2520

19
17
13
11
7
5
3 .
2 ...

19*17*13*11*7*5*3*3*2*2*2*2

20
18
16
15
14
12
10
9
8
6
4
1
'''

from fractions import gcd

def sieve(n):
    primes_list = [x for x in range(2, n+1)]
    composites_list = []
    for p in primes_list:
        c = 1
        while c*p < n:
            multiple = c*p
            if multiple in primes_list:
                composites_list.append(primes_list.pop(primes_list.index(multiple)))
            c += 1
    return (primes_list, composites_list) 

def generate_evenly_divisible_product(n):
    primes, comps = sieve(n)
    result = 1
    for p in primes:
        result *= p
    for c in comps:
        if result % c != 0:
            result *= gcd(result, c)
    return result
   
     

