## QUESTION 1

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

## Question 3

def print_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

# Example usage
print_even_numbers(17, 2)
