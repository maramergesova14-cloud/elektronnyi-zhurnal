from rest_framework import viewsets
from .models import Attendance, Grade, Student, Subject
from .serializers import (
    AttendanceSerializer,
    GradeSerializer,
    StudentSerializer,
    SubjectSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related("student", "subject").all()
    serializer_class = GradeSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related("student", "subject").all()
    serializer_class = AttendanceSerializer
