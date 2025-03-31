#01

num = int(input("Enter the number = "))

if num > 0:
    print("The number is a positive number")

elif num < 0:
    print("The number is a negative number")

else:
    print("The number is zero")


#02

no = int(input("Enter the number = "))

if no == 0:
    print("The number is neither prime nor positive")

elif no % 2 == 0:
    print("the number is even")

else:
    print("the number is odd")    

#03

a = int(input("Enter the number 1 = "))   
b = int(input("Enter the number 2 = "))

if a > b:
    print(a,"the larger number")

elif a == b:
     print("The number are equal")
      
else:
     print(b,"the larger number")    

#04
c = int(input("Enter the number= "))   

if c % 4 == 0 and c % 6 == 0:
    print("The number is divisible by 4 and 6")

else :
    print("The number not is divisible by 4 and 6")  

#5
age = int(input("Enter your age = "))
license = str(input("Do have a valid license (yes/no) ="))

if (age >= 18 and license == "yes"):
    print("You are eligble to drive")

else:
    print("You are not eligble to drive")
#6
d = input("the charecter = ")

if d.isalpha:
    print("An alphabet") 

elif d.isdigit:
    print ("A number")

else:
    print("A special charecter")
    
            