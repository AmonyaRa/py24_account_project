import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')
django.setup()
app = Celery('main_app')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# beat_schedule - периодически отправлять сообщения
app.conf.beat_schedule = {
    'send-spam': {
        'task': 'applications.account.tasks.spam_message',
        'schedule': crontab(minute='*/1')
    }
}

app.conf.beat_schedule = {
    'every': {
        'task': 'applications.spam.tasks.spam_message_user',
        'schedule': crontab(minute='*/1'),# по умолчанию выполняет каждую минуту, очень гибко
    },                                                              # настраивается

}

# твилео - по номеру телефона