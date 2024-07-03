from user import User
from sqldata import create_connection, authenticate_user, create_user
import getpass

def main():
    # Getting user input
    print("WELCOME USER!!!!")
    user_name = input("What is your name: ")
    user_name = user_name.lower()
    connection = create_connection()
    user = User(user_name, connection)
    
    print("\nPassword Manager")
    print("1. Create a new user")
    print("2. Login")
    choice = int(input("Choose an option: "))
    while choice != 1 and choice != 2:
        choice = input("Choose an option: ")
        print("Invalid option. Please try again.")
    if choice == 1:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        email = input("Enter email: ")
        create_user(connection, username, password, email)
    elif choice == 2:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        authenticate_user(connection, username, password)

    print("You have successfully logged in")
    print("\n Welcome again " + user_name)
    print(user_name + "So, What can we do for you today!!")
    while True:
        print("1. Save Password")
        print("2. Create or Suggest Password")
        print("3. Analyze Password")#modify these to analyze passwords better or the ones about to be stored
        print("4 Retrieve a password")
        print("5, change password")
        print("6. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            platform = input("What is the platform for the password: ")
            password = input("Enter the password to save: ")
            pw_valid = user.validate_pw(password)
            if not pw_valid:
                print("Password is not valid.")
                continue
            print("checking to see if reused")
            reused = user.password_reuse(password)
            if reused:
                print("it would be a good idea to use another password, password has been used. ")
                move = input("type U to use anyway and N to try again")
                move = move.lower()
                if move == "u":
                    platform = platform.lower()
                    user.set_platform(platform)
                    user.set_password(password)
                    continue
                else:
                    continue
            platform = platform.lower()
            user.set_platform(platform)
            user.set_password(password)
            
        elif choice == '2':
            platform = input("what platform is the suggested password for: ")
            platform = platform.lower()
            user.set_platform(platform)
            sug = user.password_suggester()
            reused = user.password_reuse(sug)
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
        elif choice == '6':
            user.store_passwords()
            print("Exiting the program.")
            print("BYEEEE!!! " + user_name)
            print("SEE you next time.")
            break
        elif choice == "4":
            platform = input("Which platform has the password which you wish to platform: ")
            platform = platform.lower()
            password = user.retrieve_password(platform)
            if password:
                print ("Your password is " + password)
            else:
                print("password for the " + platform + "plaform was not found" )
                print("Either you don not have a passowrd for the above platform or you spelled it wrong, can you double check and try again.")

           
        elif choice == "5":
            toChange = input(print("Which plafrom's password would you like to change "))
            update_password = input(print("What is your cuurent password"))
            success = user.password_change(toChange, update_password)
            if (success):
                print("password successfuly changes.")
            else:
                print("A problem occoured and password unsuccesfully stored.")

()
    

if __name__ == "__main__":
    main()
