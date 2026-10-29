from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, GradeViewSet

router = DefaultRouter()
router.register("grades", GradeViewSet, basename="grade")
router.register("attendance", AttendanceViewSet, basename="attendance")
urlpatterns = router.urls
