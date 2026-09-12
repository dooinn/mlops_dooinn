def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

def get_username_from_input():
    """ Not empty, no spaces """
    username = input("Tell me your username: ")

    if (username == "" or " " in username):
        print('Username is not valid.')
    else:
        return username


def get_password_from_input():
    """ At least 8 chars, 1 letter, 1 number, 1 special char """
    import re
    password = input("Tell me your password: ")

    has_letter = re.search(r"[a-zA-Z]", password)
    has_number = re.search(r"[0-9]", password)
    has_special = re.search(r"[^a-zA-Z0-9]", password)

    if (len(password) < 8 or not has_letter or not has_number or not has_special):
        print('Password is not valid.')
    else:
        return password

