from rest_framework import serializers
from ebapp.models import Users

class UsersSer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'