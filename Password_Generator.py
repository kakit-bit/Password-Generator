# Script takes user inputs to determine complexity
# Complexities include Length, Uppercase and Special Character inclusion

import random
import string

# User Input Error Check Functions
def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def in_range(value,limiter):
    if value not in range(5,limiter):
        return False
    else:
        return True

def is_yn(value):
    if value == "Y" or value == "N":
        return True
    else:
        return False

def get_passlength():
    while True:
        pass_length_string = input("Enter password length: ")
        # Check if Input is a Valid number
        if not is_number(pass_length_string):
            print("Not a valid number")
            continue
        pass_length = int(pass_length_string)
        # Check if Input for password length exceeds limitations
        if not in_range(pass_length,16):
            print("Password exceeds limitations")
            print("Password must be at least 5 characters and less than 15 characters")
            continue
        return pass_length

def get_yn(criteria):
    while True:
        question = "Include "+ criteria +" (Y/N)?: "
        case_type = input(question)
        # Check if Input is a Valid Choice
        if is_number(case_type):
            print("Not a valid input")
            continue
        pass_case = case_type.upper()
        # Check if Input Exceeds a Single Character
        if len(pass_case) != 1:
            print("Not a valid input")
            continue
        # Check if Input is (Y/N)
        if not is_yn(pass_case):
            print("Not a valid input")
            continue
        return pass_case

def pass_generator(password, length_check, case_check, special_check):
    # Generate password from numbers and lowercase letters only
    if (case_check == "N") and (special_check == "N"):
        while (len(password) < length_check):
            flip = random.randint(0, 1)
            if flip == 0:
                alpha_target = alphabet[random.randint(0, 25)]
                password.append(alpha_target)
            else:
                number_target = str(random.randint(0, 9))
                password.append(number_target)
        return password
    # Generate password from
    elif (case_check == "N") and (special_check == "Y"):
    # Generate password from numbers, lowercase letters and special characters only
        while (len(password) < length_check):
            flip = random.randint(0,2)
            if flip == 0:
                alpha_target = alphabet[random.randint(0, 25)]
                password.append(alpha_target)
            elif flip == 1:
                number_target = str(random.randint(0,9))
                password.append(number_target)
            else:
                sp_target = special_char[random.randint(0,7)]
                password.append(sp_target)
    elif (case_check == "Y") and (special_check == "N"):
        # Generate password from numbers any case type letters only
        while (len(password) < length_check):
            flip = random.randint(0, 1)
            if flip == 0:
                alpha_target = alphabet[random.randint(0, 25)]
                flip_case = random.randint(0, 100)
                if (flip_case % 2) == 0:
                    password.append(alpha_target)
                else:
                    password.append(alpha_target.upper())
            elif flip == 1:
                number_target = str(random.randint(0, 9))
                password.append(number_target)
    elif (case_check == "Y") and (special_check == "Y"):
        # Generate password from numbers and any case type letters and special characters
        while (len(password) < length_check):
            flip = random.randint(0, 2)
            if flip == 0:
                alpha_target = alphabet[random.randint(0, 25)]
                flip_case = random.randint(0, 100)
                if (flip_case % 2) == 0:
                    password.append(alpha_target)
                else:
                    password.append(alpha_target.upper())
            elif flip == 1:
                number_target = str(random.randint(0, 9))
                password.append(number_target)
            else:
                sp_target = special_char[random.randint(0, 7)]
                password.append(sp_target)

if __name__ == '__main__':
    alphabet = list(string.ascii_lowercase)
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*"]
    password = []

    length_check = get_passlength()
    case_check = get_yn("uppercase letters")
    special_check = get_yn("special characters")

    pass_generator(password, length_check, case_check, special_check)

    print("Password: " + "".join(password))





