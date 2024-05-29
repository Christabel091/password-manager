class User:
    def __init__(self, name):
        self.user_name = name
        self.user_password = None
        self.user_arr = [self.user_name]
        self.password_arr = []
        self.pform = None

    def set_password(self, password):
        # Function to store the password
        self.user_password = password
        self.password_arr.append(self.user_password)
        self.user_arr.append(self.password_arr)
        print(f"Password set for {self.user_name}")

    def password_suggester(self):
        # Function to suggest passwords
        suggested_passwords = ["password123", "1234abcd", "securePass1!"]
        print(f"Suggested passwords for {self.user_name}: {', '.join(suggested_passwords)}")
        return True

    def set_platform(self, platform):
        self.pform = platform
        self.user_arr.append(self.pform)
        print(f"Platform set to {self.pform} for {self.user_name}")

    def change_password(self, new_password):
        # Function to change the password
        pass
    def validate_pw(self,pw):
        #Function to validate the password
        tot_letter=0
        right_char=True
        up_case=False
        l_case=False
        dig=False
        alphaNum=False
        
        for chr in pw:
            tot_letter +=1
            if chr.isdigit():
                dig =True
            if chr.isalnum():
                alphaNum =alphaNum
            else:
                alphaNum=True
            if chr.isalpha():
                if chr.isupper():
                    up_case=True
                elif chr.islower():
                    l_case=True
            if chr =="@"or chr =="%" or chr =="^" or chr =="*":
                right_char =False
                
        if l_case == False or up_case == False or dig == False or alphaNum == False or right_char == False or (tot_letter < 8):
            if tot_letter < 8:
                print("Password must be at least 8 characters long")
            if l_case == False or up_case == False:
                print("password must contain both uppercase and lowercase letters")
            if dig == False:
                print("password must contain at least one digits")
            if right_char == False:
                print("password may not contain any of the following characters @, %, ^, *, ")
            if alphaNum == False:
                print("password must contain at least one of the following special characters: !, #, $. &")
            return False
        else:
            return True
    def get_arr(self):
        print(self.user_arr)
                