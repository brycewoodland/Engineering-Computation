# Given a score, display a grade

# Get input from the user
print()
score = float(input('What is your score?'))

# Determine and display the grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70:
    grade = 'C'
else:
    grade = 'Less than C'
print('Your grade is ' + grade)
print()

