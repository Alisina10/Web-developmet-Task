class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def  myfunction(abc):
        print("hello my name is",abc.name)

p1 = Person("ali",20)
p1.myfunction()


#polymoerphism Task
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

