'''
QUESTION:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

CORRECT ANSWER:
232792560

'''

from fractions import gcd

def sieve(n):
    primes_list = [x for x in range(2, n+1)]
    composites_list = list() 
    for p in primes_list:
        c = 2
        while c*p <= n:
            multiple = c*p
            if multiple in primes_list:
                composites_list.append(primes_list.pop(primes_list.index(multiple)))
            c += 1
    return primes_list, composites_list 

def doit(n):
    total = 1
    arr = [[0]]*(n+1) 
    for x in xrange(n, 1, -1):
        comp_factors = prime_factors(x)
        print "comp_factors: " +  comp_factors
        for f in comp_factors: 
            print [comp_factors.pop(comp_factors.index(num)) for num in comp_factors if num == f]
            curr_prime_list = [comp_factors.pop(comp_factors.index(num)) for num in comp_factors if num == f]
            if len(arr[f]) < len(curr_prime_list):
               arr[f] = curr_prime_list 
        print arr
    for index in range(0, n+1):
        total *= arr[index][0]*len(arr[index])
    return total


def get_index(n):
    return max(prime_factors(n))

def prod(n): 
    primes, comps = sieve(n)
    primes_copy = list(primes)
    result = 1
    for c in comps:
        composites_factors = prime_factors(c)
        for factor in composites_factors:
            if factor not in primes_copy:
                primes.append(factor)
    print primes
    for p in primes:
        result *= p
        print result
    comps = sorted(comps, key=int, reverse=True)
    print comps
    for c in comps:
        while result % c != 0:
            print "{0} mod {1} = ".format(result, c) + str(result % c)
            result *= gcd(result, c)
            comps.append(c)
            print result
    return result
   
     
def prime_factors(n):
    primes, comps = sieve(n)
    factor_list = list()
    for p in primes:
        while n % p == 0:
            factor_list.append(p)
            n = n/p
    return factor_list
