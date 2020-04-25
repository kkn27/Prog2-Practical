def main():

    password_check(password_count(input("Input the password: ")))


def password_count(password):
    while len(password) < 6:
        password = password_count(input("Password must be at least 6 words. \n >>>"))
    return password


def password_check(password):
    for i in password:
        print("*", end="")


main()
###https://github.com/kkn27/Programming2
