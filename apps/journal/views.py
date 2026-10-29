from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Attendance, Grade
from .serializers import AttendanceSerializer, GradeSerializer

class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.select_related("student", "subject").all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["student", "subject", "value", "date"]
    ordering_fields = ["date", "value"]

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.select_related("student", "subject").all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["student", "subject", "status", "date"]
    ordering_fields = ["date", "status"]
