#Author:Christabel Obi-Nwosu
#Date:November 13th 2023.
#just a reference file.
#program to set a valid password for a user.
def main():
    password_rules()
    password=input('Enter your password: ')
    pw_valid=validate_pw(password)
    while pw_valid != True:
        password=input('Enter your password:')
        pw_valid=validate_pw(password)   
    print("password set.")
            
def password_rules():
    #function to print the rules for setting a password
    print("Choose a password according to these rules:")
    print("The password must be at least 8 characters long")
    print("The password must contain both uppercase and lowercase letters")
    print("The password must contain at least one digit")
    print("The password must contain at least one of the following special characters: !, #, $, &")
    print("The password may not contain any of the following characters: @, %, ^, *")
    print()

def validate_pw(pw):
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
            
main()