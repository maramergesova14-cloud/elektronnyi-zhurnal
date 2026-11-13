from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.get_full_name", read_only=True)
    class Meta:
        model = Student
        fields = ("id", "user", "full_name", "classroom", "student_code", "birth_date", "guardian_name", "guardian_phone", "is_active")
