# Электронный журнал группы

Учебный проект на Django REST Framework для учёта студентов, учебных предметов, оценок и посещаемости.

## Модули
- `apps/accounts` — JWT-авторизация и пользователи.
- `apps/students` — студенты и группы.
- `apps/catalog` — учебные предметы.
- `apps/journal` — оценки и посещаемость.
- `apps/reports` — сводный и индивидуальный отчёты.
- `config` — настройки Django и URL-маршруты.

## Запуск в Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Проверка сервера: http://127.0.0.1:8000/  
Админ-панель: http://127.0.0.1:8000/admin/

## API
- `POST /api/auth/token/` — получить JWT по username/password.
- `POST /api/auth/token/refresh/` — обновить токен.
- `GET /api/auth/me/` — текущий пользователь.
- `/api/students/` — CRUD студентов.
- `/api/subjects/` — CRUD предметов.
- `/api/journal/grades/` — оценки.
- `/api/journal/attendance/` — посещаемость.
- `GET /api/reports/summary/` — сводная статистика.
- `GET /api/reports/students/<id>/` — отчёт студента.

API требует JWT или сессионную авторизацию. Для API-запросов передавай заголовок `Authorization: Bearer <access>`.
