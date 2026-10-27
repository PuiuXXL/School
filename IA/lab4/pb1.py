students = [
    ["Maria", 8.5],
    ["Ana", 7.0],
    ["Roxi", 10.0],
    ["Ianis", 8.5],
    ["Andreea", 7.0]
]

grades = sorted(set(grade for name, grade in students))
second_lowest = grades[1]
list_students = sorted(name for name, grade in students if grade == second_lowest)

for name in list_students:
    print(name)