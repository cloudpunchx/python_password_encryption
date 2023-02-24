# import hashlib - removed after importing SALT bcrypt
import bcrypt

# MAKE SURE PASSWORD FIELD IN DB VARCHAR IS LONG ENOUGH FOR HASH

#Realistically will come from a user's sign-up API Call instead of 'input'
while True:
    password = input("Please type a password:")
    # 12 rounds is default for gensalt(rounds=12), that is how long it takes to encrypt
    # most times its okay to leave as-is
    # (example if you put 30 rounds it could take hours to encrypt so this time affects how long it takes a user to login/signup)
    salt = bcrypt.gensalt()
    hash_result = bcrypt.hashpw(password.encode(), salt)
    # Hash result gets put in a db column under password.

    # Login POST
    # The same as a login attempt
    pass2 = input("Please enter the same password:")
    if (bcrypt.checkpw(pass2.encode(), hash_result)):
    # The code retrieve the previously hashed password from db and compares the 2.
        print("You have successfully logged in.")
    else:
        print("The login failed.")




# Need to install salt library (pip install bcrypt then import to file)
