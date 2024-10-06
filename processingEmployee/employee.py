from json import load

f=open("C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\processingEmployee\\data.json","r")

employees=load(f)

print(employees)

# q1 number of employees
print(len(employees))

# q2 all employee name
employee_names=[e.get("name") for e in employees]
print(employee_names)

# print employee names working as qa
dep_filter=[e.get ("name") for e in employees if e.get("department")=="qa"]
print(dep_filter)

# location ekm employee name
place_filter=[e.get("name") for e in employees if e.get("location")=="ekm"]
print(place_filter)
