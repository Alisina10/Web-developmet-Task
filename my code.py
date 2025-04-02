ali = 20
great_friend = False
if ali >= 18:
    if great_friend:
        print ("you are my best friend")
    else:
        print ("you are not my best friend")
else:
    print ("none of them")

    age = 19
    ticsts = True
    if age >= 18 and ticsts:
        print("you can not inter to the club")
    else:
        print("you can inter to the club")

def sum (length, width):
    area = length * width
    premeter= 2 * (length + width)
    return area, premeter
area, premeter = sum(10, 20)
print(f"area : {area}, premeter : {premeter}")


def sumall (**nums):
   for num, value in nums.items():
       print (f"{num} : {value}")
sumall(name = "ali", age = 20, gender = "male", location = "egypt")

try:
    x = int (input("Enter a number:"))
    print (10/x)
except ZeroDivisionError:
    print ("division by zero")
except ValueError:
    print ("invalid input")
else:
    print ( "Thanks for working with me", x)


    def withdraw(balance, amount):
        if amount > balance:
            raise ValueError("insufficient balance.")
        return balance - amount


    try:
        new_balance = withdraw(1000, 500)
    except ValueError as e:
        print(f"error:{e}")

        import random

        name = input("your name :")
        if name == "ali":
            print("hello ali")
        else:
            print(name)


from datetime import datetime, timedelta

current_date = datetime.now()
print (f"current_date is : {current_date}")
future_date = current_date + timedelta(days = 7)
print (f"future_date is : {future_date}")


ineventory = {

    'gold' : 500, 'cirence' : 12,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

ineventory ["gold"] += 600
if ineventory ["cirence"] > 10:
    print("we are busy now!")
    print (ineventory)


#code of OOP

class Company:
    def __init__(self, name, last_name, work_experience):
        self.name = name
        self.last_name = last_name
        self.work_experience = work_experience

    def display_info(self):  # Fixed method name
        return f"{self.name} {self.last_name} {self.work_experience}"

# Creating objects (should be outside the class)
com_1 = Company("Ali", "Ahmed", 2)
com_2 = Company("Abbas", "bahar", 3)
com_3 = Company("Mujtaba", "Jawid", 4)

# Corrected method calls
print(com_1.display_info())
print(com_2.display_info())
print(com_3.display_info())


class Uni:

    def __init__(self, name, age, gender, location):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
    def brake(self):
        return f"{self.name} This is Ali Sina Jawid"


uni_1 = Uni ("ali", 20, "male", "egypt")
uni_1.name = "ali sina jawid"
print(uni_1.brake())
print(uni_1.age)
print(uni_1.gender)


class Uni:

    def __init__(self, name, age, gender, location):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
    def brake(self):
        return f"{self.name} This is Ali Sina Jawid"


uni_1 = Uni ("ali", 20, "male", "egypt")
uni_1.name = "ali sina jawid"
print(uni_1.brake())
print(uni_1.age)
print(uni_1.gender)


class User:
    def __init__(self, name_name, password):
        self.name_name = name_name
        self.password = password

    def login(self, password):
        if self.password == password:
            return f"Welcome {self.name_name}"
        else:
            return "Wrong password"

User = User("John", "1234")


print(User.login("1234"))
print(User.login("wrong password"))


#

class BankAccount:
    def __init__(self, account_number, password):  # Fixed constructor method
        self.account_number = account_number
        self.password = password
        self.__balance = 0  # Initialize balance to 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:  # Fixed condition
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount or insufficient balance.")

    def get_balance(self):  # Fixed method name
        return self.__balance

# Creating a bank account
account = BankAccount("123456", "password")

# Performing transactions
account.deposit(500)
account.withdraw(100)
print("Balance:", account.get_balance())


#inhratence

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "animal sound"

class Dog(Animal):
    def make_sound(self):
        return "bark"

class Cat(Animal):
    def make_sound(self):
        return "meow"


dog = Dog("Fido")
cat = Cat("Fluffy")

print(dog.name, "says:",dog.make_sound())
print(cat.name,"says :", cat.make_sound())


#plomorfism

class Bird:
    def fly(self):
        return "flying High"

class Airplane:
    def fly(self):
        return "flying fast"

class finsh:
    def fly(self):
        return "I can't fly"

for onj in [Bird(), Airplane(), finsh()]:
    print(onj.fly())

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Fixed class name
    @abstractmethod
    def drive(self):
        pass  # Abstract method should not have an implementation

class Car(Vehicle):
    def drive(self):
        print("Drive method in Car class")

class Bike(Vehicle):
    def drive(self):
        print("Drive method in Bike class")

# Creating objects
car = Car()
bike = Bike()

# Incorrect method call removed
car.drive()  # This will correctly print "Drive method in Car class"
bike.drive()  # This will correctly print "Drive method in Bike class"

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
       return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"


class library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book.display())

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)

my_library = library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.display_books()



# Regular Expressions

import re
from pydoc import replace

text = "This is my phone number 1234567890 and this is my office number 9876543210"
pattern = r"\d+"
replacement = "NUMBER"

result = re.sub(pattern, replacement, text)
print(result)


#

from datetime import datetime, timedelta

# Define the current time
current_time = datetime.now()

# Calculate the future date (7 days later)
future_date = current_time + timedelta(days=7)

# Print the future date
print(f"Future date is: {future_date}")

past_data = current_time - timedelta(days=7)
print(past_data)

import time

def countdown(seconds):

    while seconds:
        print ("This remains: ", seconds, "seconds")
        time.sleep(1)
        seconds -= 2

    print ("Lift off!")

countdown(10)



#css work






var user = "ali";
let age = 22;
const country = "AFG";

console.log(user, age, country);

user = "Mujtaba";
age = "30";

console.log (user, age, country)