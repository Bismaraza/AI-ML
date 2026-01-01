# # QUESTION 1

# def get_largest( a, b, c):
#     if (a >= b) and (a >= c):
#         return a
#     elif (b >= a) and (b >= c):
#         return b
#     else:
#         return c

# print( get_largest( 0, 20, 45))

# # Question 2 
# salary = int( input(" Enter your Salary: "))

# if (salary < 30000):
#     tax = salary * (5 /100)
#     print("Your tax is: ", tax)

# elif (salary in range (30000, 70000)):
#     tax = salary * (15 /100)
#     print("Your tax is: ", tax)
# else : 
#     tax = salary * (25 /100)
#     print("Your tax is: ", tax)

# # Question 3

# def print_even_numbers(a, b):
#     start = min(a, b)
#     end = max(a, b)
    
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)

# print_even_numbers(17, 2)

# # Question 4 

# def print_digit(n):
#     while n>0: 
#         digit = n % 10
#         print(digit)
#         n = n // 10 

# print_digit(1234)

## Question 5
# num = int(input("Enter a number: "))
# count = 0
# while num> 0:
#     count += 1
#     num = num // 10

# print("The number of digits in the given number is:", count)

## Question 6 
num = int(input("Enter a number: ")) # 23 
remainder = 0 
sum = 0
while num > 0: # 2 
    remainder = num % 10  # 2
    sum= sum + remainder  # 3+2 
    num = num // 10 # num = 0 
print("The sum of digits in the given number is:", sum)

