print("My name is sri varshava kumar")

#day4 prb set 1 basics
#1
x,y,z = [4,8,12]
print(f"{x}")
print(f"{y}")
print(f"{z}")

#2
x=1
y=2
print(f"{x}")
print(f"{y}")

x,y=y,x
print(f"{x}")
print(f"{y}")

#3
p=q=r=100
print(f"{p}")
print(f"{q}")
print(f"{r}")

#prb set 2 unpacking
#4
x,y,z = [4,8,12]
print(f"{x} , {y} , {z}")

#5
a,b,c = "DOG"
print(f"{a} , {b} , {c}")

#6
x,*z,y = (1,2,3,4,5)
print(f"{x} , {y} , {z}")

a=3
b=2
c=a%b
print(c)

d=a//b
print(d)

num=6
result = (num>0) and (num%2 == 0)
print("The number is positive and even", result)

text = "I LOVE PYTHON"
check= "python"  not in text
print(check)

l = 10
b = 2

area = l*b
peri = 2*(l+b)

print("area = ", area)
print("perimeter = ", peri)

e=14.97//3
print(e)

