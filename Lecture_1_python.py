# Question 1
name = str(input("Enter Your Name:"))
age = int(input("Enter Your age:"))

print("Hello",name,",You are", age, "years Old!")

#Question 2
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Question 3
num1 = int(input("Enter first integer number:"))
num2 = int(input("Enter second integer number:"))
num3 = float(input("Enter first float number:"))

num1= float(num1)
num2= float(num2)

average= (num1 +num2 +num3)/3

print("The average of three numbers is:", average)

#Question 4
num1 = input("Enter first number:")

num2=int(num1)
num3=float(num1)
num4=str(num1)

print(num2, type(num2))
print(num3, type(num3))
print(num4, type(num4))


# Question 5 

x = 10 + 3* 2 **2
# step 1: 2 ** 2 = 4
# step 2: 3 * 4 = 12
# step 3: 10 + 12 = 22
print(x)

#Question 6
a = 10
b = 5
c =12

swap = a
a = b
b =c
c = swap

print("The value of a after swapping:", a)
print("The value of b after swapping:", b)
print("The value of c after swapping:", c)


