from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ebapp.models import *
from ebapp.serializers import *

class RegisterAPIView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSer