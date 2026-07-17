student ={
    "name" :"adithyakrishna",
    "age" :20,
    "course":"MCA"
}
print("orginal dictionary:")
print(student)
print("\n student name:",student["name"])
print("\n student age:",student["age"])
student["grade="]= "A"
print("\nafter adding grade :")
print(student)
removed=student.pop("age")
print("\ndictionary after removal:")
print(student)
print("\nkey-value pairs:")
for key,value in student.items():
    print(key,":",value)
