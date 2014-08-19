'''
QUESTION: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

CORRECT ANSWER: 233168
'''

def sum3or5(start_num, max_num):
    '''
    :param start_num: start counting from this number
    :param max_num: stop at this number (inclusive)
    :return the sum of all natural numbers who are multiples of 3 or 5
    '''
    total = 0
    for x in range(start_num, max_num):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total 

# list comprehension: do (<this> to <x>) for <x> in <list>

def sumz(start, max):
    return sum([x for x in range(start, max) if x % 3 == 0 or x % 5 == 0])

