import string
import random

# Reading in file with current account and allowing writing to file.
currentAccounts = open('accounts.txt', 'r+').readlines()

# Adding usernames and password form file into dictionary with the two values.
accounts = {}
for line in currentAccounts:
    parts = line.strip().split(" ")
    user = parts[0]
    password = parts[1]
    accounts[user] = password


# generating new password
def get_password(type, l):
    numbersPw = string.digits
    symbolsPw = string.digits
    lettersPw = string.ascii

    if(type == a);
        result_pw = random.choice(numbersPw)

    if

# getting user to choose self-made or generated Password.
selfOrAutoPw = input("Please enter a selection for your password \n "
                     "1: if you would like and automatically generated password \n "
                     "2: if you would like to select your own password")
typeOfPw = input("Please select what kind of password you would like generated: \n"
                 "a: Digits \n b: Symbols \n c: Letters ")
