import time

def checking_characters(password, safety_score):
    if any(char in "!,$,%,&" for char in password):
        print("Your password contains special characters, OK!")
        safety_score += 1
    else:
        print("Your password does not contain special characters...CHANGE!")
        safety_score -= 1
    time.sleep(1)
    return safety_score

def checking_numbers(password, safety_score):
    if any(char.isdigit() for char in password):
        print("Your password contains numbers, OK!")
        safety_score += 1
    else:
        print("Your password does not contain numbers, NOT OK")
        safety_score -= 1
    time.sleep(1)
    return safety_score

def check_length(password, safety_score):
    if len(password) > 8:
        print("Your password has more than 8 characters, OK!")
        safety_score += 1
    else:
        print("Your password has less than 8 characters, CHANGE!")
        safety_score -= 1
    time.sleep(1)
    return safety_score

# Main code
password = input("Input your password here: ")
safety_score = 0

safety_score = checking_characters(password, safety_score)
safety_score = checking_numbers(password, safety_score)
safety_score = check_length(password, safety_score)

print("Your safety score for the password is:", safety_score)
