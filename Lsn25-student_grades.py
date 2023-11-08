# Get input from the user
print()
num_students = int(input('How many students do you need to enter grades for? '))

# Initialize lists
students = []
grades = []

# Build Lists
print()
for i in range(num_students):
    new_student = input(f'Name of student #{i+1}: ').capitalize()
    new_grade = float(input(f'Grade for {new_student}: '))
    students.append(new_student)
    grades.append(new_grade)
    print()
print()

# Print results
print('\nStudent  Grades')
for i in range(len(students)):
    print(f'{students[i]:<10} {grades[i]:.0f}')
print()

average = sum(grades)/(len(grades))
max_grade = grades[0]
max_student = students[0]
min_grade = grades[0]
min_student = students[0]
print(f'The average grade is {average} ')
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
