"""
#1
def myFunction(grams):
    ounces = 28.3495231 * float(grams)
    print(ounces)

grams = input()
myFunction(grams)

#2
def FahrenheitToCentigrade(fahrenheit):
    centigrade = (5 / 9) * (float(fahrenheit) - 32)
    print(centigrade)

fahrenheit = input()
FahrenheitToCentigrade(fahrenheit)
"""

"""
#3
def solve(numheads, numlegs):
    rabbits = (numlegs - (numheads * 2)) / 2
    chickens = numheads - rabbits
    print("rabbits: ", int(rabbits))
    print("chickens: ", int(chickens))

numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)
"""

"""
#4
import math 
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def filter(numbers_input):
    prime_numbers = []
    for num in numbers_input:
        if isPrime(int(num)):
            prime_numbers.append(num)
    return prime_numbers

numbers_input = input().split()
prime_numbers = filter(numbers_input)

for num in prime_numbers:
    print(num, end = " ")
"""
"""
#5
def toString(List): 
    return ''.join(List) 

def permute(a, l, r):
    if l == r:
        print(toString(a), end = " ")
    else:
        for i in range (l,r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
string = str(input())

n = len(string)
a = list(string)

permute(a, 0, n - 1)
"""


"""
#6
def reverse(inputedSentence):
    eachWord = inputedSentence.split()
    reversedSentence = ' '.join(eachWord[::-1])
    return reversedSentence

mySentence = input()
reversedMySentence = reverse(mySentence)
print(reversedMySentence)
"""

"""
#7
def has_33(nums):
    for i in range (0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

numlist = [int(x) for x in input().split()]
print(has_33(numlist))
"""


"""
#8
def spy_game(nums):
    spy = [0, 0, 7]
    for num in nums:
        if num == spy[0]:
            spy.pop(0)
        if len(spy) == 0:
            return True
    return False

numlist = [int(x) for x in input().split()]
print(spy_game(numlist))
"""

"""
#9
def volumeOfSphere(radius):
    formula = (4/3) * 3.14 * (radius**3)
    return formula

rad = float(input())
print(volumeOfSphere(rad))
"""

"""
#10
def uniquelist(mylist):
    newlist = []
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist

items = list(input())

newuniquelist = uniquelist(items)

for item in newuniquelist:
    if item == ' ':
        newuniquelist.remove(item)

print(newuniquelist)
"""

"""
#11
def is_palindrome(myword):
    myword = myword.lower()
    if myword == myword[::-1]:
        return "YES"
    else:
        return "NO"

word = str(input())
print(is_palindrome(word))
"""

"""
#12
def histogram(mylist):
    for item in mylist:
        print("*"*int(item))

input_list = input().split()
histogram(input_list)
"""

"""
#13
import random

def guessNumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20")
    number = random.randint(1,20)
    guessesnum = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guessesnum += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guessesnum} quesses!")
            break

guessNumber()
"""