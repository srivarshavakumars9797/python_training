#Task1, assigning values

a=5
b=a
a =a +1
print(a)

b=2
b += 5
print(b)

c=10
d=c **2
print(d)

#Task2
length = 11
length %= 3
print(length)

#Task3
x = 7
x *= 3
print(x)

#Task4
a = 10
b = 2
a /= b
print(a)

#Task5
height1 = 15
height2 = 13
print(height1 != height2)

#Task6
print((5 + 3) < (2 * 5))

#Task7
age = 20
print(age >= 18)

#Task8
height = 6
print((height >5) and (height<10))

#Here's the order of operator precedence in Python from highest to lowest:

#Exponentiation: **
#Unary operators: ~
#Multiplication, division, floor division, and modulus operators: *, /, //, %
#Addition and subtraction operators: +, -
#Relational operators: <, >, <=, >=
#Equality operators: ==, !=
#Logical AND operator: and
#Logical OR operator: or
#Assignment operators: =, +=, -= 

#Task9
val=3+2*10/2
print(val)

#Left-Associative:
#On Left-Associative Operators, operations are performed from left to right. Most operators are left-associative. 
# For instance, in (A - B + C), addition and subtraction, being left-associative, will first evaluate (A - B), and then add (C) to the result.

#result = 10 - 2 + 3  # Both - and + have the same precedence and are left-associative
#print(result)       # Output: 11 ((10 - 2) + 3 is evaluated as 8 + 3)

#result = 10 / 2 * 3  # Both / and * have the same precedence and are left-associative
#print(result)       # Output: 15.0 ((10 / 2) * 3 is evaluated as 5.0 * 3)


#Right-Associative:
#Although less common, some operators are right-associative, meaning they are evaluated from right to left. 
# An example is the exponentiation operator **.
#In (2 ** 2 ** 3) Python will first calculate (2 ** 3) which is 8 and then calculate 2*8 which evaluates to 256.

#result = 2 ** 2 ** 3  # Exponentiation is right-associative
#print(result)        # Output: 256 (2 ** (2 ** 3) is evaluated as 2 ** 8)

#Task10
print(2 ** 1 ** 3)

y = 4
z = 2

print("sum = ", y+z)
print("sub = ", y-z)
print("mul = ", y*z)
print("div = ", y/z)
print("rem = ", y%z)
print("pow = ", y**z)
print("flo = ", y//z)

y += z
print(y)

val = 5
w= val<5
print(not w)

v = " I love PYTHON programing"
print("I" in v)
print("l" not in v)
