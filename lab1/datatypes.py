#EXAMPLES FROM THE ARTICLE
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#Getting the Data Type
x = 5
print(type(x))

#Setting the Data Type
x = "Hello World" #str
x = 20	#int	
x = 20.5 #float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#Setting the Specific Data Types
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry")) #tuple	
x = range(6) #range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview


#EXERCISES
#ex1
x = 5
print(type(x))

int

#ex2
x = "Hello World"
print(type(x))

str

#ex3
x = 20.5
print(type(x))

float

#ex4
x = ["apple", "banana", "cherry"]
print(type(x))

list

#ex5
x = ("apple", "banana", "cherry")
print(type(x))

tuple

#ex6
x = {"name": "John", "age" : 36}
print(type(x))

dict

#ex7
x = True
print(type(x))

bool

