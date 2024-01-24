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
