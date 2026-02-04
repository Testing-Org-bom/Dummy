import random

def password_generate(choice):
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lower = "asdfghjklqwertyuiopzxcvbnm"
    number = "0456789123"
    symbols = "!@#$%^&*?"
    allowed_symbols = input("Enter the allowed symbols (Type NA or na for default symbols): ")
    length = int(input(f'Enter the length of the {choice}: '))
    
    if(not (allowed_symbols=="NA" or allowed_symbols=="na")):
        symbols =  allowed_symbols
        
    validation_string = upper + lower + number + symbols
    password = "".join(random.sample(validation_string,length))
    print(password)
    return password
