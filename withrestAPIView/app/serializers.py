from dataclasses import field
from rest_framework import serializers
from app.models import Employee

class NameSerailizer(serializers.Serializer):
    name = serializers.CharField()

from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"