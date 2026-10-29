from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "teacher_name"]
    ordering_fields = ["name", "teacher_name"]
