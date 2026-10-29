from rest_framework import serializers
from .models import Attendance, Grade

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.StringRelatedField(source="student", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = Grade
        fields = ["id", "student", "student_name", "subject", "subject_name", "value", "date", "comment", "created_at"]

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.StringRelatedField(source="student", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = Attendance
        fields = ["id", "student", "student_name", "subject", "subject_name", "date", "status", "comment"]
