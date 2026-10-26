from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, GradeViewSet, StudentViewSet, SubjectViewSet

router = DefaultRouter()
router.register("students", StudentViewSet)
router.register("subjects", SubjectViewSet)
router.register("grades", GradeViewSet)
router.register("attendance", AttendanceViewSet)

urlpatterns = router.urls
