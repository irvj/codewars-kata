"""
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html
Examples

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.


-----------
BIGGER PERSONAL HINT --- it's actually a math problem, not necessarily a programming problem.
You need to know that trailing zeros can be counted in a factorial based on number of 5s in prime factors.

"""


def zeros(n):
    zero_counter = 0
    while (n >= 5):
        n //= 5
        zero_counter += n
    return zero_counter


"""
My first answer that calculates the factorial and times out on very large factorials...

import math

def zeros(n):
    number = math.factorial(int(n))
    count = 0
    for i in str(number)[::-1]:
        if i == '0':
            count += 1
        else:
            break
    return count
"""
