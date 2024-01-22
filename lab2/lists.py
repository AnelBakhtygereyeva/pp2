#EXERCISES-------------------------------------------------------------------------
#ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#EXAMPLES FROM THE ARTICLE----------------------------------------------------------

#Lists
mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

#list items with indexes[]
#list can be ordered and changeable

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#can contain different datatypes
list1 = ["abc", 34, True, 40, "male"]

#type()
#<class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#starting from the beginning
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#from 2 to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Changing the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Changing the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The Syntax
newlist = [expression for item in iterable if condition == True]

#Condition
newlist = [x for x in fruits if x != "apple"]

#condition with no if statement
newlist = [x for x in fruits]

#Iterable
newlist = [x for x in range(10)]

#accept numbers only lower than 5
newlist = [x for x in range(10) if x < 5]

#Expression
#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort List Alphanumerically
#alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
#words
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#numbers
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort(unexpexted result)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#Copy a List
#copy method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#List Methods
"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

