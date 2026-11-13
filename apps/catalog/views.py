from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ClassRoom, Subject
from .serializers import ClassRoomSerializer, SubjectSerializer

class ClassRoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassRoom.objects.select_related("year", "class_teacher").all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
