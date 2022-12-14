import time

from django.core.mail import send_mail
from main_app.celery import app

@app.task
def spam_message():
    send_mail(
        'Привет мы из py24',
        'Как дела?',
        'musabekova.amina13@gmail.com',  # от кого
        ['leiurus8@gmail.com']  # кому
    )