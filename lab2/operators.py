#EXAMPLES FROM THE ARTICLE----------------------------------------------------------------------------------------
#Python operators
print(10 + 5)

#Arithmetic Operators
#   +	- Addition	        x + y	
#   -	- Subtraction	    x - y	
#   *	- Multiplication	x * y	
#   /	- Division	        x / y	
#   %	- Modulus	        x % y	
#   **	- Exponentiation	x ** y	
#   //	- Floor division	x // y

#Assignment Operators
"""
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3	    x = x // 3	
**=	    x **= 3	    x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3
"""

#Comparison Operators
"""
==	- Equal	                        x == y	
!=	- Not equal	                    x != y	
>	- Greater than	                x > y	
<	- Less than	                    x < y	
>=	- Greater than or equal to	    x >= y	
<=	- Less than or equal to	        x <= y
"""

#Logical Operators
"""
and  - Returns True if both statements are true	                    x < 5 and  x < 10	
or	 - Returns True if one of the statements is true	            x < 5 or x < 4	
not	 - Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
"""


#Identity Operators
"""
is 	    - Returns True if both variables are the same object	    x is y	
is not  - Returns True if both variables are not the same object	x is not y
"""

#Membership Operators
"""
in 	    - Returns True if a sequence with the specified value is present in the object	        x in y	
not in	- Returns True if a sequence with the specified value is not present in the object	    x not in y
"""

#Bitwise Operators
"""
& 	-AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	-OR	                        Sets each bit to 1 if one of two bits is 1	                                                                x | y	
^	-XOR                        Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
~   -NOT	                    Inverts all the bits	                                                                                    ~x	
<<	-Zero fill left shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
>>	-Signed right shift	        Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
"""
#Operator Precedence
#parentheses has the highest precedence
print((6 + 3) - (6 + 3))

#multiplication has higher precedence than addition
print(100 + 5 * 3)


#precedence table highest -> lowest
"""
()	                        Parentheses	
**	                        Exponentiation	
+x  -x  ~x                  Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                Multiplication, division, floor division, and modulus	
+  -	                    Addition and subtraction	
<<  >>	                    Bitwise left and right shifts	
&	                        Bitwise AND	
^	                        Bitwise XOR	
|	                        Bitwise OR	

==  !=  >  >=  <  <=        Comparisons, identity, and membership operators	
is  is not  in  not in 

not	                        Logical NOT	
and                         AND	
or	                        OR
"""

#left to right
print(5 + 4 - 7 + 3)

#EXERCISES---------------------------------------------------------------------------------------------------------

#ex1
print(10 * 5)

#ex2
print(10 / 2)

#ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#ex4
if 5 != 10:
    print("5 and 10 is not equal")

#ex5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")