'''
QUESTION:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

CORRECT ANSWER:

906609
'''

def largest_palindrome_backwards():
    '''
    iterate downwards (by 1s) from the largest possible number
    and if that number is a palindrome, check if it also has two
    three-digit factors.
    '''
    pal = 999*999 
    while pal > 100*100:
        rev = int(str(pal)[::-1])
        if pal == rev:
            if factors(pal):
                for f in factors(pal):
                    if len(str(f)) == 3 and len(str(pal/f)) == 3:
                        return pal
        pal -= 1
    return "No palindromes with three digit factors"

def factors(n):
    '''
    -reduce applies the function in the first argument iteratively across all the members of the iterable in the second argument, left to right.
    -list.__add__ is the built-in python function that lists use to add themselves together
    -the list comprehension calculates which numbers divide N evenly, up to the square root of N
    -we want factors to be an efficient, non repetitive set of numbers
    ''' 
    factors = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n%i==0)))
    return factors

'''
some scribbles

998001
997799
996699
995599
994499

a b c c b a

a = 9
b = 9
c = 7
# number of 6 digit combos
(1 * 1 * 8) + (9 * 8 * 9)

a = 9, b = 9, c in range(0, 8)
a in range(1, 9), b in range(1, 9), c in range(1, 9)

# number of 5 digit combos
a b c b a

a in range(1, 10), b in range(0, 10), c in range(0, 10)
10000
'''

def sadness():
    '''
    this method doesn't work because the number in the inner loop decrements too fast.
    you will find a "large" palindrome with two three-digit factors, but it's not 
    necessarily the largest.
    '''
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i*j
            reverse = int(str(product)[::-1])
            if (product - reverse) == 0:
                return product
    return "No palindromes found"
