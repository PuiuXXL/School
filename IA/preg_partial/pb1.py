students = [
    ["Elev1",10],
    ["Elev2",9],
    ["Elev3",9],
    ["Elev4",8]
]

grades = sorted(set(grade for name, grade in students))
second_lowest = grades[1]
list_students = sorted(name for name,grade in students if grade == second_lowest)

for student in list_students:
    print(student)