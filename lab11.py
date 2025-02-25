#task1
list = [10,20,30,40,50]
list.append(60)
list.insert(1,15)
list.remove(30)
list.reverse()
list.sort()
print (list)

#task2
print (list[:3])
print (list[-2:])
print (list[::-1])

#task3

dectionary = {
    "name" : "ali",
    "age" : 20,
    "grade" : "A"
}

dectionary ["subject"] = "math"
dectionary ["grade"] = "A+"
dectionary.pop("age")
print (dectionary.values())
print (dectionary.keys())
print (dectionary.items())

#task4
set1 =[1,2,3,4,5]
set2 =[4,5,6,7,8]
union_set =(set1.union(set2))
difference_set = (set1.difference(set2))
intersection_set = (set1.intersection(set2))

print (union_set)
print (difference_set)
print (intersection_set)

#task5
color = ["red", "blue", "green", "red", "yellow"]

print (color.index("green"))
print (color.count("red"))

#task6

company = {
    "employee": [
        {
            "name": "Ravi", "position": "developer", "salary": 10000, "gender": "male", "location": "Egypt"
        },
        {
            "name": "Ahmed", "position": "designer", "salary": 2000, "gender": "male", "location": "Egypt"
        },
    ]
}


company["employee"].append({
    "name": "Ali", "position": "Manager", "salary": 4000, "gender": "male", "location": "Afghanistan"
})


for employee in company["employee"]:
    print("Name:", employee["name"])
    print("Position:", employee["position"])
    print("Salary:", employee["salary"])
    print("Gender:", employee["gender"])
    print("Location:", employee["location"])
    print("-" * 20)
