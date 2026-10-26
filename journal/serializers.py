from rest_framework import serializers
from .models import Attendance, Grade, Student, Subject


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.__str__", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = Grade
        fields = ["id", "student", "student_name", "subject", "subject_name", "value", "date", "comment"]


class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.__str__", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = Attendance
        fields = ["id", "student", "student_name", "subject", "subject_name", "date", "status"]
