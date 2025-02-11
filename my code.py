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