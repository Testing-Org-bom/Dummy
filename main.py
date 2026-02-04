from utils.passwordgenerator import password_generate
from utils.captchagenerator import captcha_generator

def generator():
    while True:
        choice = int(input("Enter the Choice:\n 1: Password Generation\n 2. Captcha Generation\n"))
        if choice == 1:
            password_generate("Password")
            break
        elif choice == 2:
            captcha_generator()
            break
        else:
            print("Please enter the write choice")
            
if __name__ == "__main__":
    generator()
