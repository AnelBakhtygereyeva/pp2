#1 - Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""
import re

def patternMatch(someString):
    pattern = '^a(b*)$'
    if re.search(pattern, someString):
        return("It's a match!")
    else:
        return("It's not a match:()")

text = input()
print(patternMatch(text))
"""

#2 - Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
"""
import re

def patternMatch(someString):
    pattern = 'a(b{2,3})$'
    if re.search(pattern, someString):
        return("It's a match!")
    else:
        return("It's not a match:()")

text = input()
print(patternMatch(text))
"""

#3 - Write a Python program to find sequences of lowercase letters joined with a underscore.
"""
import re

def patternMatch(someString):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, someString):
        return("Found the sequence!")
    else:
        return("There is no such sequence:()")

text = input()
print(patternMatch(text))
"""


#4 - Write a Python program to find the sequences of one upper case letter followed by lower case letters.
"""
import re

def patternMatch(someString):
    pattern = '^[A-Z][a-z]+$'
    if re.search(pattern, someString):
        return("Found the sequence!")
    else:
        return("There is no such sequence:()")

text = input()
print(patternMatch(text))
"""

#5 - Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
"""
import re

def patternMatch(someString):
    pattern = 'a.*?b$'
    if re.search(pattern, someString):
        return("It's a match!")
    else:
        return("It's not a match:()")

text = input()
print(patternMatch(text))
"""

#6 - Write a Python program to replace all occurrences of space, comma, or dot with a colon.
"""
import re

text = input()
print(re.sub("[ ,.]", ":", text))
"""

#7 - Write a python program to convert snake case string to camel case string.
"""
import re

def snakeToCamel(word):
    return "".join(x.capitalize() or "_" for x in word.split("_"))

snake = input()
print(snakeToCamel(snake))
"""

#8 - Write a Python program to split a string at uppercase letters.
"""
import re

myString = str(input())
words = re.findall('[A-Z][^A-Z]*', myString)

print(words)
"""

#9 - Write a Python program to insert spaces between words starting with capital letters.
"""
import re

def spaceBetweenCapital(words):
    withSpace = re.findall('[A-Z][^A-Z]*', words)
    return withSpace

myString = str(input())

words = spaceBetweenCapital(myString)
print(' '.join(words))
"""

#10 - Write a Python program to convert a given camel case string to snake case.
"""
import re

def camelToSnake(myText):
    camelString1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', myText)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camelString1).lower()

text = input()
print(camelToSnake(text))
"""