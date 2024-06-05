from user import User

def main():
    # Getting user input
    print("WELCOME USER!!!!")
    user_name = input("What is your name: ")
    user = User(user_name)
    
    while True:
        print("\n Welcome " + user_name)
        print("1. Save Password")
        print("2. Create or Suggest Password")
        print("3. Analyze Password")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            platform = input("What is the platform for the password: ")
            password = input("Enter the password to save: ")
            pw_valid = user.validate_pw(password)
            if not pw_valid:
                print("Password is not valid.")
                continue
            print("checking to see if reused")
            reused = user.password_used(password)
            if reused:
                print("it would be a good idea to use another password, password has been used. ")
                move = input("type u to use anyway and p to try againy")
                move = move.lower()
                if move == "u":
                    user.set_platform(platform)
                    user.set_password(password)
                    continue
                else:
                    continue
            user.set_platform(platform)
            user.set_password(password)
        elif choice == '2':
            platform = input("what platform is the suggested password for: ")
            user.set_platform(platform)
            sug = user.password_suggester()
            reused = user.password_used(sug)
            if reused:
                print("it would be a goo idea to use another password, password has been used. ")
                move = input("type u to use anyway and p to try againy")
                move = move.lower()
                if move == "u":
                    user.set_platform(platform)
                    user.set_password(password)
                else:
                    continue
            user.set_password(sug)
            print("Password suggested:", sug)
        elif choice == '3':
            user.analyze_strength()
        elif choice == '4':
            print("Exiting the program.")
            print("BYEEEE!!! " + user_name)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
