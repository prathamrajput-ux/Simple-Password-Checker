current_password = "Pratham"
while True :
    user_password = input("Enter Your Password :" )
    if current_password == user_password:
        print("Corect Password , Congrats !")
        break
    else :
        print("invalid password , try again..!")
print("Logined ")