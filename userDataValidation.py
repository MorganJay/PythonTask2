import random
import string
from _collections import defaultdict


def get_user_details():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    email_address = input('Email Address: ')
    # introduced a check for valid email addresses
    email_checker = True
    while email_checker:
        if '@' in email_address:
            if len(email_address) > 4:
                users_details = [first_name, last_name, email_address]
                return users_details
                break
            else:
                email_checker = True
                email_address = input('Please enter a valid email address ')
        else:
            email_address = input('Please enter a valid email address ')


def password_generator(user_details):
    characters = string.ascii_letters
    numbers = string.digits
    random_password = ''.join(random.choice(characters + numbers) for i in range(5))
    password = str(user_details[0][:2] + user_details[1][-2:] + random_password)
    return password


# program initializes
status = True
active_users = {'First Name:': '', 'Last Name:': '', 'Email Address:': '', 'Password:': ''}

while status:
    # obtain user information
    user_details = get_user_details()
    # call to generate random password
    password = password_generator(user_details)
    # display generated password and request user input
    password_choice = input(f"Would you like to use the suggested password? {password} Enter yes or no ")
    if password_choice == 'yes':
        user_details.append(password)
        # entering user information to active container which is a dictionary
        active_users = defaultdict(list)
        active_users['First Name:'].append(user_details[0])
        active_users['Last Name:'].append(user_details[1])
        active_users['Email Address:'].append(user_details[2])
        active_users['Password:'].append(user_details[3])
    else:
        password = input("Please enter a password with at least 7 characters")
        password_len = True
        while password_len:
            if len(password) < 7:
                password = input('Password must be at least 7 characters ')
            else:
                user_details.append(password)
                active_users = defaultdict(list)
                active_users['First Name:'].append(user_details[0])
                active_users['Last Name:'].append(user_details[1])
                active_users['Email Address:'].append(user_details[2])
                active_users['Password:'].append(user_details[3])
                password_len = False
                break
    new_user = input('Would you like to add another user? yes or no ')
    if new_user == 'no':
        status = False
        # format the output of registered users to improve readability
        [print(user, value) for user, value in active_users.items()]
        print('\nThanks for using my program 😁')
        break
