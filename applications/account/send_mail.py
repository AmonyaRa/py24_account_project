import time

from django.core.mail import send_mail


def send_hello(email):
    send_mail(
        'Вас приветствует наш сайт',
        'Привет! Как дела?',
        'musabekova.amina13@gmail.com',
        [email]
    )

def send_confirmation_email(email, code):
    time.sleep(5)
    full_link= f'http://http://127.0.0.1:8000/account/activate/{code}/'
    send_mail(
        'Активация пользователя',
        full_link,
        'musabekova.amina13@gmail.com',
        [email]
    )

def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'musabekova.amina13@gmail.com',
        [email]
    )

