passwords = [{'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
{'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}]

def date_password(passwords, date):
    # This will filter and return a list of dictionaries where the 'added_on' matches the date parameter
    return [password for password in passwords if password['added_on'] == date]

# Example usage:
filtered_passwords = date_password(passwords, '21/03/22')
print(filtered_passwords)
