from django.db.models import Avg, Count, Q
from apps.clients.models import Student
from apps.orders.models import Grade, Attendance

def get_summary():
    grade_stats = Grade.objects.aggregate(average=Avg("value"), total=Count("id"))
    attendance_total = Attendance.objects.count()
    absent_total = Attendance.objects.filter(status=Attendance.Status.ABSENT).count()
    late_total = Attendance.objects.filter(status=Attendance.Status.LATE).count()
    return {
        "students_total": Student.objects.filter(is_active=True).count(),
        "grades_total": grade_stats["total"] or 0,
        "average_grade": round(grade_stats["average"], 2) if grade_stats["average"] is not None else None,
        "attendance_records": attendance_total,
        "absences_total": absent_total,
        "late_total": late_total,
        "attendance_rate_percent": round((attendance_total - absent_total - late_total) * 100 / attendance_total, 2) if attendance_total else None,
    }
