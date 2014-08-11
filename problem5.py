'''
QUESTION:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

CORRECT ANSWER:
232792560

'''

import math

def prod(n):
    """Generate the smallest positive number that is evenly divisible by all the
    numbers from 1 to n.

    The lcm of all the numbers from 1 to n is the union of all the sets of
    primes in the prime factorization of each number. This solution calculates
    the answer iteratively.
    """ 

    prod_array = [[1]]*(n+1)
    for number in range(n, 1, -1):
        factors = prime_factors(number)
        for factor in factors:
            group = [value for index, value in enumerate(factors) if value == factor]
            if len(prod_array[factor]) <= len(group):
                prod_array[factor] = list(group) 
    total = 1
    for index in range(len(prod_array)):
        total *= prod_array[index][0]**len(prod_array[index])
    return total

def brute_force(n):
    """Should do the same thing as prod.
    """
    number = 1
    check = False
    while number <= math.factorial(n):
        for i in range(1, n+1):
            if number % i != 0:
                check = False
                break
            else:
                check = True
        if check == True:
            return number
    return None

def prime_factors(n):
    """Returns the prime factorization of n in a list.
    """
    primes, comps = sieve(n)
    factors_list = list()
    for prime in primes:
        while n % prime == 0:
            factors_list.append(prime)
            n = n / prime 
    return factors_list


def sieve(n):
    """The sieve of eratosthenes, used to extract primes (and composites)
    from a list of numbers 1 to n.
    """
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

