print('Enter student names and their grades.')
print()

students = []
grades = []
name = 'initial name'

while name != 'End':
    name = input("Enter student name ('end' to quit): ").capitalize()
    if name != 'End':
        grade = float(input(f'Enter grade for {name}: '))
        print()
        students.append(name)
        grades.append(grade)
print()

print('Student   Grades')
for i in range(len(students)):
   print(f'{students[i]:<10} {grades[i]:<15}')
print()

average = sum(grades)/(len(grades))
max_grade = grades[0]
max_student = students[0]
min_grade = grades[0]
min_student = students[0]
print(f'The average grade is {average:.1f} ')
for i in range(len(students)):
    if grades[i] > max_grade:
        max_student = students[i]
        max_grade = grades[i]
    if grades[i] < min_grade:
        min_student = students[i]
        min_grade = grades[i]
print(f'{max_student} had the highest grade of {max_grade:.0f}')
print(f'{min_student} had the lowest grade of {min_grade:.0f}')
print()
