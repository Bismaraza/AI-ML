# Question 1

age = int(input(" Enter your age:"))

if age>= 18:
    print("You can Vote")
   
else:
    print("You cannot Vote")


print("Thank you")

# Question 2 

color= input("Enter the color of the traffic light:")
if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Wait")
elif color == "Green":
    print("Go")
else: 
    print("Invalid color")

# Question 3 
age = int(input("Enter your age:"))
if age <= 13:
    print("Child")
elif age > 13 and age < 18:
    print("Teenager")
else:
    print("Adult")

# Question 4

username = input("Enter your username:")
password = input("Enter your password:")

if (username == "admin" and password == "pass"):
    print("Login successful")
elif (username != "admin"):
    print("Wrong username")
else:
    print("Wrong password")