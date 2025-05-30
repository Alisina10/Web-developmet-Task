# write a funaction to check if a number is prime
def prime(num):
    if num <= 1:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(prime(7))
print (prime(12))

#Write a function to calculate the square of a number.
def square(num):
    return num ** 2
print(square(5))

#Create a function that takes a list of numbers and returns their sum.
def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4, 5]))

#Implement a recursive function to calculate the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))