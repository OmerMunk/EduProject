from rest_framework import serializers
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        depth = 1


class TestsExecutedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestExecuted
        fields = '__all__'
        depth = 1






