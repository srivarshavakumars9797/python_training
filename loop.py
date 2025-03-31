#problem 1
a = 0

if a > 0:
    print("The number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")

#problem 2
b = 0

if b ==0:
    print("Number is neither odd nor even")
elif b%2 == 0:
    print("The number is even")

elif b%2 != 0:
    print("The number is odd")  

#Here the condition of zero should give first as zero is divided by two then the remainder will be zero then the loop stops and print zero has even number.

#problem 3
age = 5

if age >= 18:
    print ("Eligible to vote")

else:
    print(" Not eligble to vote")

#problem 4
x = 5
y = 3
z = 1

if ((x>y) and (x>z)):
    print("The largest number is", x)

elif y>z:
    print("The largest number is ", y)

else:
    print("The largest number is ", z)

#problem 5
c = 5

if ((c % 5 == 0) and (c % 11 == 0)):
    print("The number is divisible by 5 and 11")

else:
    print("The number is not divisible by 5 and 11")

#problem 6
year = 2000

if (((year % 4 == 0)and (year % 100 != 0)) or (year % 400 == 0)):
    print("The year is leap year")

else:
    print("The year is not a leap year")

#problem 7
mark =99

if mark>=90:
    print("A grade")

elif ((mark<90) and (mark>=75)):
    print("B grade")
      
elif ((mark<75) and (mark>=50)):
    print("C grade")      

else:
    print("Fail")

#problem 8
char = "a"

if char in "aeiou":
    print ("vowel")

else:
    print("consonant")    
  
#problem 9
num = 1

if (num ==0):
    print("Number is neither odd nor even")

elif ((num%2 == 0) and (num >0)):
    print("The number is positive and even")

elif ((num%2 != 0) and (num >0)):
    print("The number is positive and odd")  

else :
    print("The number is negative")

#problem 10
angle1 =45
angle2 =45
angle3 =90

if (angle1 + angle2 + angle3 == 180):
    print("the triangle is valid")

else :
    print("the triangle is not vaid")

#problem11
a , b, c = [1,4,1/4]

des= b**2-(4*a*c)
if des >= 0:
    print("Real roots",des)

else :
    print("Imaginary roots",des)

#problem12

#problem13
d = 12

if ((d % 2 == 0)and(d % 4 == 0)):
    print("The number is Even and divisible by 4")

elif ((d % 2 == 0)and(d % 4 != 0)):
    print("The number is Even and not divisible by 4")

elif ((d % 2 != 0)and(d % 4 != 0)):
    print("The number is Odd and not divisible by 4")

#problem14
char = "ajlgldnblnlmlnm"

if char.isalpha():
    print("It is an alphabet")

else:
    print("It is not an alphabet")    

#problem15
e = 15
f = 22   

if e>f:
    print("The largest number is ",e)

else:
    print ("Then largest number is ",f)

#problem16
temp = 36.5

if temp < 0:
    print("below the freezing point")

elif temp == 0:
    print("at freezing point")
  
else :
    print("above the freezing point")
 
#problem17
units = 500

if units <=100:
    bills = units*5
    print("The Electric bill is Rs",bills)

elif units <=200:
    bills = 100*5 + (units - 100)*7
    print("The Electric bill is Rs",bills)

else :
    bills = 100*5 + 100*7 + (units - 200)*10
    print("The Electric bill is Rs",bills)

#problem18

#problem19
weight = 100
height = 60.5

bmi = weight / (height**2)

if bmi <18.5:
    print("underweight")

elif bmi >= 25:
    print("overweight")

else:
    print("normal")

#problem20
alp = "AAAS"

if alp.isupper():
    print("it upper case")

elif alp.islower():
    print("it lower case")

else:
    print("not a letter")
