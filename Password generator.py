#importing required modules
import random
import string

#Function for password generator
def password_generator(min_len,num=True,sym=True):
    letter=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    characters=letter
    if num:
        characters+=digits
    if sym:
        characters+=symbols
    
    pass_word=""
    meets_criteria=False
    has_num=False
    has_sym=False
    while not meets_criteria or len(pass_word)<min_len:
        ch=random.choice(characters)
        pass_word+=ch
        if ch in digits:
            has_num=True
        elif ch in symbols:
            has_sym=True
        meets_criteria=True
        if num:
            meets_criteria=has_num
        if sym:
            meets_criteria=meets_criteria and has_sym
    return pass_word
#Main program
min_length=int(input("Enter minimum length of password:"))
print("Mention complexity of password:")
number=input("Do you want numbers(y/n):").lower()=='y'
special_char=input("Do you want special characters(y/n):").lower()=='y'
pwd=password_generator(min_length,number,special_char)
print("Generated password:",pwd)

    

