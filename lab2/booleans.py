#EXAMPLES FROM THE ARTICLE
#Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#if statement
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

#two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#with a __len__ function
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

# yes or no
def myFunction() :
  return True

if myFunction():
  print("YES!")

  
else:
  print("NO!")

#built-in functions
x = 200
print(isinstance(x, int))

#EXERCISES
#ex1
print(10 > 9)

True

#ex2
print(10 == 9)

False

#ex3
print(10 < 9)

False

#ex4
print(bool("abc"))

True

#ex5
print(bool(0))

False