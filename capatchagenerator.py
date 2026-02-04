from captcha.image import ImageCaptcha
from passwordgenerator import password_generate

def captcha_generator():
    image = ImageCaptcha(width = 280, height = 90)
    captcha = password_generate("captcha")
    print(captcha)
    data = image.generate(captcha)
    image.write(captcha, 'CAPTCHA.png')
