grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_students = {}
students = sorted(students)

for key in range(len(students)):
    grades_students[students[key]] = sum(grades[key]) / len(grades[key])

print(grades_students)