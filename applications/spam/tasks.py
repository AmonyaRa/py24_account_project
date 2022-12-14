import time

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from applications.spam.models import Spam
from main_app.celery import app


@app.task
def spam_message_user():
    emails = Spam.objects.all()
    # 3 вариант
    send_mail(
        'Привет мы из py24',
        'Это спам',
        'musabekova.amina13@gmail.com',  # от кого
        [i.email for i in emails])

    # 2 вариант

    # list_email = [i.email for i in emails]
    # send_mail(
    #     'Привет мы из py24',
    #     'Это спам',
    #     'musabekova.amina13@gmail.com',  # от кого
    #     list_email  # кому
    # )

    # 1 вариант
    # for i in emails:
    #     send_mail(
    #         'Привет мы из py24',
    #         'Это спам',
    #         'musabekova.amina13@gmail.com',  # от кого
    #         [i.email]  # кому
    #     )
