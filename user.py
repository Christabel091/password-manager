import random
import string
import re
from sqldata import passwordReuse, store_password, store_platform, get_user_id, retrievePassword, passwordChange
from ceaser import generate_cipher, encode_message, decode_message
class User:
    def __init__(self, name, connection):
        self.user_name = name
        self.user_password = None
        self.password_arr = []
        self.pform_arr = []
        self.pform = None
        self.connection = connection
        self. cipher = generate_cipher(6)

    def set_password(self, password):
        encrypted_password = encode_message(password, self.cipher)
        self.user_password = encrypted_password
        self.password_arr.append(self.user_password)
        print(f"Password set for {self.user_name}")

    def password_suggester(self):
        char_set = string.ascii_letters + string.digits + string.punctuation
        length = 12
        random_string = ''.join(random.choice(char_set) for _ in range(length))
        print(random_string)
        print("password suggested")
        return random_string

    def set_platform(self, platform):
        self.pform = platform
        self.pform_arr.append(self.pform)
        print(f"Platform set to {self.pform} for {self.user_name}")

    def store_passwords(self):
        user_id = get_user_id(self.connection, self.user_name)
        if user_id is None:
            print("User ID not found for username:", self.user_name)
            return
        for pw, platform in zip(self.password_arr, self.pform_arr):
            password_id = store_password(self.connection, user_id, pw)
            if password_id:
                store_platform(self.connection, user_id, password_id, platform)

    def validate_pw(self, pw):
        tot_letter = 0
        right_char = True
        up_case = False
        l_case = False
        dig = False
        alphaNum = False

        for chr in pw:
            tot_letter += 1
            if chr.isdigit():
                dig = True
            if chr.isalnum():
                alphaNum = True
            if chr.isalpha():
                if chr.isupper():
                    up_case = True
                elif chr.islower():
                    l_case = True
            if chr in "@%^*":
                right_char = False

        if not (l_case and up_case and dig and alphaNum and right_char and tot_letter >= 8):
            if tot_letter < 8:
                print("Password must be at least 8 characters long")
            if not (l_case and up_case):
                print("Password must contain both uppercase and lowercase letters")
            if not dig:
                print("Password must contain at least one digit")
            if not right_char:
                print("Password may not contain any of the following characters: @, %, ^, *")
            if not alphaNum:
                print("Password must contain at least one of the following special characters: !, #, $, &")
            return False
        return True

    def analyze_strength(self):
        weights = {
            'length': 0.2,
            'uppercase': 0.2,
            'lowercase': 0.2,
            'digit': 0.2,
            'special_char': 0.1,
            'common_pattern': 0.1,
        }

        for pw in self.password_arr:
            length_criteria = len(pw) >= 12
            uppercase_criteria = bool(re.search(r'[A-Z]', pw))
            lowercase_criteria = bool(re.search(r'[a-z]', pw))
            digit_criteria = bool(re.search(r'[0-9]', pw))
            special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pw))

            common_patterns = ["123456", "password", "qwerty", "admin", "letmein", self.user_name, "Password12#", (self.user_name + "123#")]
            common_pattern_criteria = not any(pattern in pw.lower() for pattern in common_patterns)

            strength = (
                weights['length'] * length_criteria +
                weights['uppercase'] * uppercase_criteria +
                weights['lowercase'] * lowercase_criteria +
                weights['digit'] * digit_criteria +
                weights['special_char'] * special_char_criteria +
                weights['common_pattern'] * common_pattern_criteria
            )

            strength_percentage = int(strength * 100)

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

    def retrieve_password(self, platform):
        user_id = get_user_id(self.connection, self.user_name)
        if user_id is None:
            print("User ID not found for username:", self.user_name)
            print("you will have to create a new user or put the proper username ")
            return
        encrypted_password = retrievePassword(self.connection, platform, user_id)
        if encrypted_password:
            decrypted_password = decode_message(encrypted_password, self.cipher)
            return decrypted_password
        return None



    def password_reuse(self, apassword):
        user_id = get_user_id(self.connection, self.user_name)
        if user_id is None:
            print("User ID not found for username:", self.user_name)
            print("you will have to create a new user or put the proper username ")
            return
        
        passwords = passwordReuse(self.connection, user_id)
        for password in passwords:
            decrypted_password = decode_message(password, self.cipher)
            if decrypted_password == apassword:
                return True
        return False

    def password_change(self, platform, new_password):
        user_id = get_user_id(self.connection, self.user_name)
        if user_id is None:
            print("User ID not found for username:", self.user_name)
            print("You will have to create a new user or put the proper username.")
            return
        encrypted_password = encode_message(new_password, self.cipher)
        success = passwordChange(self.connection, user_id, platform, encrypted_password)
        return success
