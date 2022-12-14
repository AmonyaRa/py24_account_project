import time

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from applications.spam.models import Spam
from main_app.celery import app



@app.task
def spam_message_user():
    email = Spam.objects.all()
    for i in email:
        send_mail(
            'Привет мы из py24',
            'Это спам',
            'musabekova.amina13@gmail.com',  # от кого
            [i.email]  # кому
        )
