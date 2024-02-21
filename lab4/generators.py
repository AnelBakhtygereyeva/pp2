#1 - Create a generator that generates the squares of numbers up to some number N
"""
def Squares(N):
    for i in range(1, N+1):
        yield i**2

b = int(input())
a = Squares(b)

for num in a:
    print (num)
"""

#2 - Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
"""
def evenNumbers(n):
    for i in range(2, n+1, 2):
        yield i

n = int(input())
evenNumbersSequence = list(evenNumbers(n))
print(','.join(str(num) for num in evenNumbersSequence))
"""

#3 - Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
"""
def dividedBy3And4(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in dividedBy3And4(n):
    print(num)
"""

#4 - Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
"""
def Squares(a,b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())
n = Squares(a,b)

for num in n:
    print (num)
"""

#5 - Implement a generator that returns all numbers from (n) down to 0.
"""
def toZero(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for num in toZero(n):
    print(num)
"""