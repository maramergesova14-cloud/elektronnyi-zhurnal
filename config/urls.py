from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from apps.catalog.views import ClassRoomViewSet, SubjectViewSet
from apps.clients.views import StudentViewSet
from apps.orders.views import LessonViewSet, GradeViewSet, AttendanceViewSet
from apps.reports.views import SummaryAPIView

router = DefaultRouter()
router.register("classes", ClassRoomViewSet)
router.register("subjects", SubjectViewSet)
router.register("students", StudentViewSet)
router.register("lessons", LessonViewSet)
router.register("grades", GradeViewSet)
router.register("attendance", AttendanceViewSet)

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/reports/summary/", SummaryAPIView.as_view(), name="report-summary"),
]
