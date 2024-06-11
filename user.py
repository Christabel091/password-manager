import random
import string
import re


class User:
    def __init__(self, name):
        self.user_name = name
        self.user_password = None
        self.password_arr = []
        self.pform_arr = []
        self.pform = None

    def set_password(self, password):
        # Function to store the password
        self.user_password = password
        self.password_arr.append(self.user_password)
        print(f"Password set for {self.user_name}")

    def password_suggester(self):
        # Function to suggest passwords
        # Define the character set to include letters, digits, and special characters
        char_set = string.ascii_letters + string.digits + string.punctuation
        length = 12

        # Generate a random string of the specified length
        random_string = ''.join(random.choice(char_set) for _ in range(length))
        print(random_string)
        print("password suggested")
        return random_string

    def set_platform(self, platform):
        self.pform = platform
        self.pform_arr.append(self.pform)
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
        
                
    def password_used(self, password):
        for pw in self.password_arr:
            if pw == password:
                return True
        return False



    def analyze_strength(self):
        for pw in self.password_arr:
            weights = {
                'length': 0.2,
                'uppercase': 0.2,
                'lowercase': 0.2,
                'digit': 0.2,
                'special_char': 0.1,
                'common_pattern': 0.1,
            }
            
            length_criteria = len(pw) >= 12
            uppercase_criteria = bool(re.search(r'[A-Z]', pw))
            lowercase_criteria = bool(re.search(r'[a-z]', pw))
            digit_criteria = bool(re.search(r'[0-9]', pw))
            special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pw))
            
            common_patterns = ["123456", "password", "qwerty", "admin", "letmein", self.user_name, "Password12#",(self.user_name + "123#") ]
            common_pattern_criteria = not any(pattern in pw.lower() for pattern in common_patterns)
            
            # Calculate strength
            strength = (
                weights['length'] * length_criteria +
                weights['uppercase'] * uppercase_criteria +
                weights['lowercase'] * lowercase_criteria +
                weights['digit'] * digit_criteria +
                weights['special_char'] * special_char_criteria +
                weights['common_pattern'] * common_pattern_criteria
            )
            
            # Convert strength to percentage
            strength_percentage = int(strength * 100)
            
            # Feedback
            feedback = []
            if not length_criteria:
                feedback.append("Password should be at least 12 characters long.")
            if not uppercase_criteria:
                feedback.append("Password should include at least one uppercase letter.")
            if not lowercase_criteria:
                feedback.append("Password should include at least one lowercase letter.")
            if not digit_criteria:
                feedback.append("Password should include at least one digit.")
            if not special_char_criteria:
                feedback.append("Password should include at least one special character.")
            if not common_pattern_criteria:
                feedback.append("Password should not contain common patterns or easily guessable sequences.")
            
            print(f"Password: {pw}")
            print(f"Strength: {strength_percentage}%")
            for f in feedback:
                print(f)
            print()
