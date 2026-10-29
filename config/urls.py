from django.contrib import admin
from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class HealthView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def get(self, request):
        return Response({"status": "ok", "project": "Электронный журнал группы"})

urlpatterns = [
    path("", HealthView.as_view(), name="health"),
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/students/", include("apps.students.urls")),
    path("api/subjects/", include("apps.catalog.urls")),
    path("api/journal/", include("apps.journal.urls")),
    path("api/reports/", include("apps.reports.urls")),
]
