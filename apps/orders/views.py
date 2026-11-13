from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Lesson, Grade, Attendance
from .serializers import LessonSerializer, GradeSerializer, AttendanceSerializer

class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.select_related("classroom", "subject", "teacher").all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Grade.objects.select_related("student__user", "lesson", "teacher").all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AttendanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attendance.objects.select_related("student__user", "lesson").all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
