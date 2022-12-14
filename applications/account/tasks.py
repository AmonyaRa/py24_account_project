import time

from django.core.mail import send_mail
from main_app.celery import app

@app.task
def send_confirmation_email_celery(email, code):
    time.sleep(10)
    full_link= f'http://http://127.0.0.1:8000/account/activate/{code}/'
    send_mail(
        'Активация пользователя',
        full_link,
        'musabekova.amina13@gmail.com',
        [email]
    )

@app.task
def spam_message():
    send_mail(
        'Привет мы из py24',
        'Как дела?',
        'musabekova.amina13@gmail.com',  # от кого
        ['leiurus8@gmail.com']  # кому
    )
