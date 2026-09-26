correct_username = "dimsxz25"
correct_password = "dimas123"

input_username = input("Input your username: ")

if input_username == correct_username:
    input_password = input("Input your password: ")
    if input_password == correct_password:
        print("Login successfull!")
    else :
        print("Invalid password.")
else:
        print("Invalid username.")