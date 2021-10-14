from rest_framework import serializers
from snippets.models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['firstname','lastname','teachername','classname','schoolname']
