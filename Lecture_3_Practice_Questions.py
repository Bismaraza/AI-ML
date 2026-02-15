## String is Palindrome or not
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