from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.students.models import Student
from .services import build_summary, student_report

class SummaryReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(build_summary())

class StudentReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, student_id):
        if not Student.objects.filter(pk=student_id).exists():
            raise Http404("Студент не найден")
        return Response(student_report(student_id))
