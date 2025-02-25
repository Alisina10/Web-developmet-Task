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

# Correct indentation (no extra spaces before `company`)
company["employee"].append({
    "name": "Ali", "position": "Manager", "salary": 4000, "gender": "male", "location": "Afghanistan"
})

# Corrected `for` loop
for employee in company["employee"]:
    print("Name:", employee["name"])
    print("Position:", employee["position"])
    print("Salary:", employee["salary"])
    print("Gender:", employee["gender"])
    print("Location:", employee["location"])
    print("-" * 20)  # Separator for readability
