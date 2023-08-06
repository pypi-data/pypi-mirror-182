# a secure secret key generator for django
#!/usr/bin/env python

import string
import secrets
import re

# a secure secret key generator for django
# a function to act as the cli for the module
def main():
    # get the key length from the user
    key_length = get_key_length()
    
    while key_length < 128:
        print('Key length must be at least 128 characters.\n')
        key_length = get_key_length()
    # get the key
    key = generate(key_length)
    while not test_key(key):
      print('Key generation failed. Trying again...')
      key = generate(key_length)
    # print the key
    pretty_print(key)

#get key length from user
def get_key_length():
    # get the key length from the user
    key_length = input('Enter the length of the key (default - 128): ')
    # if the user did not enter a key length
    if key_length == '':
        print('Using default key length of 128 characters.\n')
        # set the key length to 128
        key_length = 128
    else:
        # convert the key length to an integer
        key_length = int(key_length)
    # return the key length
    return key_length

# pretty print the key so its easier to read and copy create a nice looking key
def pretty_print(key):
    # print the key so that it is easier to read and copy
    print('Key: ' + key)
    # print the key length
    print('Key length: ' + str(len(key)))
    # print the number of unique characters in the key
    print('Number of unique characters: ' + str(len(set(key))))


# a function to generate the key
def generate(key_length):
    # get the characters to use in the key
    chars = string.ascii_letters + string.digits + string.punctuation
    # generate the key
    key = ''.join(secrets.choice(chars) for _ in range(key_length))
    # return the key
    return key


def test_key(key):
    # check the length of the key
    if len(key) < 128:
        return False
    # check the number of unique characters in the key
    if len(set(key)) < 5:
        return False
    # check that the key contains at least one lowercase letter
    if not re.search(r'[a-z]', key):
        return False
    # check that the key contains at least one uppercase letter
    if not re.search(r'[A-Z]', key):
        return False
    # check that the key contains at least one digit
    if not re.search(r'\d', key):
        return False
    # check that the key contains at least one special character
    if not re.search(r'[^a-zA-Z\d]', key):
        return False
    # check that the key does not contain any easily guessable words or patterns
    if re.search(r'(password|123456|qwerty)', key, re.I):
        return False
    return True


# if the module is run as a script
if __name__ == "__main__":
    # run the main function
    main()
