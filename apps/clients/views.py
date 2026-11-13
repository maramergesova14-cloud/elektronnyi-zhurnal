from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.select_related("user", "classroom").all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
