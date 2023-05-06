login_db = "JohnDoe"
password_db = "Gwi@zdA#99"

attempts = 0
i = 1;
while i <= 3 and attempts == 0:
    login = input("Login: ")
    password = input("Password: ")
    if login == login_db and password == password_db:
        print("Logging in successful")
        attempts = 1
    else:
        print("Error logging in! Attempts left: ", 3-i)
        i = i + 1
