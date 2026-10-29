from django.urls import path
from .views import StudentReportView, SummaryReportView

urlpatterns = [
    path("summary/", SummaryReportView.as_view(), name="summary-report"),
    path("students/<int:student_id>/", StudentReportView.as_view(), name="student-report"),
]
