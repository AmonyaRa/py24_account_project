from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Spam(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email