from  user import User

def main():
    #getting inputs
    print("WELCOME USER!!!!")
    user_name = input("What is your name: ")
    user = User(user_name)
    password = input("Enter the password to save today: ")
    platform = input("What is the platform for the passowrd")
    user.set_platform(platform)
    pw_valid=user.validate_pw(password)
    if pw_valid != True:
        print("\n\npassword is not a valid password and has low strength")
        print("You can validate the password or i can suggest something new ")
        action = input("say YES to suggest and NO to validate ")
        while action != "YES" and action != "NO":
            print("wrong input")
            password=input('Enter your password:')
        if action == "YES":
            sug = user.password_suggester()
        elif action == "NO":
            password=input('Enter your password:')
            pw_valid=user.validate_pw(password) 
    if pw_valid == True:
        user.set_password(password)
    else:
        print("failed")
        #implement suggestion function later
    
    

        
if __name__ == "__main__":
    main()
