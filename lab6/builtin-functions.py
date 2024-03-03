#1 - Write a Python program with builtin function to multiply all the numbers in a list
"""
from functools import reduce

numbers = [int(x) for x in input().split()]
result = reduce(lambda x, y: x * y, numbers)

print(result)
"""

#2 - Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
"""
myString = input("The string:")

upperLetters = sum(1 for char in myString if char.isupper())
lowerLetters = sum(1 for char in myString if char.islower())

print("Uppers: ", upperLetters)
print("Lowers: ", lowerLetters)
"""

#3 - Write a Python program with builtin function that checks whether a passed string is palindrome or not.
"""
def isPalindrome(string):
    return string == string[::-1]

myString = input("The string: ")
if isPalindrome(myString):
    print("Is palindrome :)")
else:
    print("Is not a palindrome :(")
"""

#4 - Write a Python program that invoke square root function after specific milliseconds.

"""
The time.sleep() function
 is used to pause the execution 
 of the program for a specified 
 number of seconds (or milliseconds in this case). 
 In the given context, it is used to introduce a delay
before calculating the square root of a number. 
This delay simulates waiting for a specific 
amount of time before performing the calculation.
"""

'''
import time
import math
def isqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = int(input())
milliseconds = int(input())
result = isqrt(number, milliseconds)

print({f"Square root of {number} after {milliseconds} is {result}"})
'''

#5 - Write a Python program with builtin function that returns True if all elements of the tuple are true.
"""
x = (False, True, True)
result = all(x)
print(result)

#or

x = (True, True, True)
result = all(x)
print(result)
"""