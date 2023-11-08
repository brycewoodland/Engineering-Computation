
students = ['Chris','Jack','Susan']
scores = [87,71,93]

print(f'The current students are {students}. ')
print(f'Their grades are {scores}. ')

choice = input(('Do you want to ADD or REMOVE a student? '))
if choice.lower() == 'add':
    new_student = input('What is the name of the student you want to add? ')
    students.append(new_student.capitalize())
    new_grade = int(input('What is the grade for the added student? '))
    scores.append(new_grade)
    print(f'The list of your students is now {students} ')
    print(f'Their grades are {scores}. ')
elif choice.lower() == 'remove':
    stud_remove = int(input('What is the number of the student to remove? '))
    students.pop(stud_remove-1)
    scores.pop(stud_remove-1)
    print(f'The list of your students is now {students}. ')
    print(f'Their grades are {scores}. ')
else:
    print('You did not enter a valid option.')
