
#try
try:
    print("Hello")
except:
    print("Error")
else:
    print("Done")


#else
try:
    print("Hello")
except:
    print("Error")
finally:
    print("Done the work")


#finally
try:
    f = open ("test.txt")
    try:
        f.write("Hello")
    finally:
        f.close()
except:
    print("Error")

#Rise the exception
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
