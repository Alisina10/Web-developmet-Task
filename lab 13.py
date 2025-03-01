import re
# Lab 1
text = "This number in mine 543-7867 and this number is not mine 123-4567 but this is your number 123-4567"
pattern = r"\d{3}-\d{4}"

result = re.findall(pattern, text)
print(" This is my phone number ", result)

#lab 2

text1 = "Hello my name is ali"
text2 = "John where are you brother"

pattern1 = r"ali"
pattern2 = r"John"

result1 = re.search(pattern1, text1)
result2 = re.match(pattern2, text2)

print("This is my name", result1)
print("This is my name", result2)

#lab 3

text = "This is my number 123-4567 but this is not my number 543-7867"
pattern = r"\d+"

result = re.sub(pattern, "NUMBER", text)
print(result)

#lab 4
text = "There are all all Email alisinajawid555@gmail.com, alisinajawid554@gmail.com, alisinajawid556@gmail.com and alisinajawid575@gmail.com"

pattern = r"\b\w+@\w+\.\w+\b"

result = re.findall(pattern, text)
print("This is my email", result)

#lab 5
text = "My country is Saudi Arabia"
pattern = r"\b[aeiou]\w*\b"

result = re.findall(pattern, text, re.IGNORECASE)
print("This is my country", result)