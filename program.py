# Warmup: convert lower case characters to uppercase and vice versa
# import sys
# for line in sys.stdin:
#     s = ''
#     for c in line.strip():
#         if c.islower():
#             c = c.upper()
#         elif c.isupper():
#             c = c.lower()
#         print(c, end='')
#     print('')



# conditional expression
def abc(x):
    # if x > 100:
    #     return 'big'
    # return 'small'
    # conditional expression
    return 'big' if x > 100 else 'small'



#p attern matching replacing p[0] and p[1] with x,y
# l = [(1,2), (3,4), (5,6)]

# # for p in l:
# #     x = p[0]
# #     y = p[1]
# #     print(f'x = {x}, y = {y}, sum = {x+y}')

# for x,y in l:
#     print(f'x = {x}, y = {y}, sum = {x+y}')


# list comprehensions
def squares(n):
#     l = []
#     for i in range(1, n+1):
#         l.append(i*i)
#     return l

    return [i * i for i in range(1, n+1)]



# generate copy of l with all elements+1
def add1(l):
    return [i+1 for i in l]



# read two numbers on a single line and print output a = 4, b = 15, sum = 19
# a, b = [int(word) for word in input.split()]


# list comprehension with f clause
# [x for x in range(30) if x % 5 == 2]


# euler problem 1
def euler1():
    return sum([x for x in range(1000) if x % 5 == 0 or x % 3 == 0])

# nested loop in list comprehension
# [(i, j) for i in range(1, 4) for j in range(1, 4)]

#return list of all elements in nested arrays [[1,2,3],[4,5,6]] --> [1,2,3,4,5,6]
def flatten(m):
    return [e for row in m for e in row]



################################# RECURSION ################################



# function that computes n! recursively

def factorial(n):

    # ITERATIVE
    # p = 1
    # for i in range(1, n+1):
    #     p *= i
    # return p

    # RECURSIVE
    # BASE CASE
    # if n == 1:
    #     return 1

    # # RECURSIVE CASE
    # return n * factorial(n-1)

    #RECURSION IN ONE LINE
    return 1 if n == 1 else n * factorial(n-1)


def orange(n):
    if n == 0:
        return

    orange(n-1)
    print('orange')


# Euclid's algorithm
#   a   b  
#   b   a%b

def gcd(a, b):
    # BASE CASE
    # if b == 0:
    #     return a

    # # RECURSIVE CASE
    # return gcd(b, a%b)

    # SINGLE LINE
    return a if b == 0 else gcd(b, a%b)



# FIBONNACI NUMBERS
# fib(1) = 1
# fib(2) = 1
# fib(3) = 2

# if k > 2 fib(k-1) + fib(k-2)

def fib(k):
    if k <= 2:
        return 1

    return fib(k-1) + fib(k-2)