"""
#1
class String:
    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())

str = String()
str.getString()
str.printString()
"""

"""
#2-3
class Shape:
    def __init__(self):
        self.areavalue = 0

    def area(self):
        print("shape area: ", self.areavalue)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        self.areavalue = self.length * self.length
        print("square area:", self.areavalue)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        self.area_value = self.length * self.width
        print("rectangle area:", self.area_value)

length_square = int(input())
shape_square = Square(length_square)
shape_square.area()

length_rec = int(input())
width_rec = int(input())
shape_rectangle = Rectangle(length_rec,width_rec)
shape_rectangle.area()
"""

"""
#4
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new.x 
        self.y = new.y 

    def dist(self, secondPoint):
        retur((self.x - secondPoint.x)**2 + (self.y - secondPoint.y)**2)**0.5
"""

"""
#5
class Account:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not available")

my_name = str(input())
how_much = int(input())
log = Account(my_name, how_much)

log.deposit(500)
log.withdraw(2000)
log.withdraw(700)

print(log.balance)
"""

"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


numbers = list(input())
prime_numbers = list(filter(lambda x: x.strip() != '' and is_prime(int(x)), numbers))
print(prime_numbers)
"""



mile = [1.0, 6.5, 9]
kilometer = list(map((lambda x: x * 1,6 ,mile)))
print(kilometer)