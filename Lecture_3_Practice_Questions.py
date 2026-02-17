# String is Palindrome or not
text = "madam"
reverse_string = ""
idx=0

for ch in text:  
    reverse_string = ch + reverse_string 
print(reverse_string)
if(reverse_string == text):
    print("Pilandrome")
else:
    print("Not")


# Average f numbers in list
my_list = [1,2,3,4,5]
sum = 0
for num in my_list:
    sum = sum+ num
    print(sum)

average = sum / len(my_list)
print(average)

# Input two list from user
list1 = list(input("Enter a list 1: "))
list2 = list(input("Enter list 2: "))

print(list1)
print(list2)

print(type(list1))

final_list = list1+ list2
print(final_list)
final_list.sort()
print(final_list)


# Question 4 
tup = (2,3,4,5,6,7,8,9)
tup1 = ()
tup2 =()


for i in tup:
    if (i % 2 ==0): 
        tup1 = tup1 + (i,)

    else:
        tup2 =  tup2 + (i,)

print("Even is ", tup1)
print("odd is:", tup2)


# Question 5

my_dict = {
    "Raza" : 67
}
print(my_dict)
option = input((" Enter a key to perofom task(A,B,C,D):"))
match option :
    case "A":
        print("--- Add a Student ----")
        name = input(" Enter the name:")
        mark = int(input("Enter marks "))
        my_dict[name] = mark

    case "B":
        print("--- Update Marks ---")
        name = input(" Enter the name you want to update:")
        if(name in my_dict):
            new_mark = input("Enter marks ")
            my_dict[name] = new_mark
        else:print("Student not found")


    case "C":
        print("--- Search for a student ---")
        name = input(" Enter the name you want to find:")
        if(name in  my_dict):
            print(my_dict[name])
        else: print("Student not found")

    case "D":
        print("--- Display All Students & Marks ---")
        for name, mark in my_dict.items():
            print(name, mark)
    case _:
        print("Invalid Choice")
print(my_dict)


# Question 6 
words = ["Apple", "Banana", "Kiwi","Cherry", "Mango"]
length = len(words[1])

print(length)

new_dict = {}
for i in words:
    length = len(i)
    new_dict[i]= length
print(new_dict)

# Question 7 
text = input("Enter a string: ")
print("Number of spaces:", text.count(" "))

