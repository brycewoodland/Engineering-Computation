# Determine if a student can graduate with honors
print()
gpa_cutoff = float(input("What is your GPA?"))
essay = input('What is your essay category?')

if gpa_cutoff >= 3.7 and essay.lower() == 'excellent' or essay.lower() == 'very good':
    honor = True
else:
    honor = False
if honor:
    print('Congratulations! You can graduate with honors!')
else:
    print('You are not eligible to graduate with honors.')
print()

