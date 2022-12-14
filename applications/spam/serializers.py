from django.contrib.auth import get_user_model
from rest_framework import serializers
from applications.spam.models import Spam
from django.core.mail import send_mail
from main_app.celery import app

User = get_user_model()


class SpamSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(required=False) # чтобы не запрашивал email, а чтобы брал его с токеном

    class Meta:
        model = Spam
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.email
        spam = Spam.objects.create(email=user, **validated_data)
        return spam
