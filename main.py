class User:
    def __init__(self, name):
        self.user_name = name

    def password_suggester(self):
        # Function implementation
        pass

    def change_password(self):
        # Function implementation
        pass

def main():
    print("WELCOME USER!!!!")
    user_name = input("What is your name: ")
    user = User(user_name)

if __name__ == "__main__":
    main()
