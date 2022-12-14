from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.spam.models import Spam
from applications.spam.serializers import SpamSerializer


# Create your views here.
class SpamApiView(ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
