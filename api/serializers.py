from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import birthday_data


class birthdayserializer(serializers.ModelSerializer):
    class Meta:
        model = birthday_data
        fields = ['name','id','user_id','date']
    