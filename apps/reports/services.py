from django.db.models import Avg
from apps.journal.models import Attendance, Grade
from apps.students.models import Student

def build_summary():
    return {
        "students_total": Student.objects.filter(is_active=True).count(),
        "grades_total": Grade.objects.count(),
        "average_grade": Grade.objects.aggregate(value=Avg("value"))["value"],
        "attendance_total": Attendance.objects.count(),
        "attendance_absences": Attendance.objects.filter(status=Attendance.ABSENT).count(),
        "attendance_late": Attendance.objects.filter(status=Attendance.LATE).count(),
    }

def student_report(student_id):
    grades = Grade.objects.filter(student_id=student_id).select_related("subject").order_by("-date")
    attendance = Attendance.objects.filter(student_id=student_id).select_related("subject").order_by("-date")
    return {
        "student_id": student_id,
        "grades": [{"subject": g.subject.name, "value": g.value, "date": g.date, "comment": g.comment} for g in grades],
        "attendance": [{"subject": a.subject.name, "status": a.status, "date": a.date, "comment": a.comment} for a in attendance],
    }
