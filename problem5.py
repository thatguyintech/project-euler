'''
QUESTION:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

CORRECT ANSWER:
232792560

'''
def sieve(n):
    primes_list = [x for x in range(2, n+1)]
    composites_list = []
    for p in primes_list:
        c = 2
        while c*p <= n:
            multiple = c*p
            if multiple in primes_list:
                composites_list.append(primes_list.pop(primes_list.index(multiple)))
            c += 1
    return primes_list, composites_list 

     
def prime_factors(n):
    primes, comps = sieve(n)
    factors_list = list()
    for prime in primes:
        while n % prime == 0:
            factors_list.append(prime)
            n = n / prime 
    return factors_list


def prod(n):
    prod_array = [[1]]*(n+1)
    primes, composites = sieve(n)
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
