first_name = input('What is your first name?')
last_name = input('What is your last name?')
email_address = input('What is your email address?')
phone_number = input('What is your phone number?')
job_title = input('What is your job title?')
id_number = input('What is your ID number?')
print('\n')
print('Please enter the following information:')
print('\n')
print('First Name:' + ' ' + first_name.upper())
print('Last Name:' + ' ' + last_name.lower())
print('Email Address:' + ' ' + email_address)
print('Phone number:' + ' ' + phone_number)
print('Job Title:' + ' ' + job_title.title())
print('ID number:' + ' ' + id_number)
print('\n')
print('The ID Card is:') 
print('------------------------------------------')
print(last_name.upper() + ',' + ' ' + first_name.capitalize())
print(job_title.title())
print('ID:' + id_number)
print('\n')
print(email_address.lower())
print(phone_number)
print('------------------------------------------')