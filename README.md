# Электронный журнал группы

Учебный проект на Django REST Framework для учёта студентов, учебных предметов, оценок и посещаемости.

## Модули
- `apps/accounts` — JWT-авторизация и пользователи.
- `apps/students` — студенты и группы.
- `apps/catalog` — учебные предметы.
- `apps/journal` — оценки и посещаемость.
- `apps/reports` — сводный и индивидуальный отчёты.
- `config` — настройки Django и URL-маршруты.

## Требования
- Windows 10/11 и PowerShell.
- Python 3.12 (рекомендуется).
- PostgreSQL 17 (для основного варианта запуска).

## Запуск с PostgreSQL в Windows PowerShell

1. Склонируй репозиторий и перейди в его папку.
2. Установи PostgreSQL и запомни пароль пользователя `postgres`.
3. Создай базу данных с именем `journal`. Это можно сделать в SQL Shell (psql), выполнив:

```sql
CREATE DATABASE journal;
```

4. Создай и активируй виртуальное окружение, затем установи зависимости:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

5. Создай локальный файл настроек:

```powershell
Copy-Item .env.example .env
```

6. Открой `.env` и укажи свой пароль PostgreSQL в `POSTGRES_PASSWORD`. Не публикуй этот файл и не отправляй его в GitHub.

7. Примени уже имеющиеся миграции, создай администратора и запусти сервер:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Открой сайт: http://127.0.0.1:8000/  
Админ-панель: http://127.0.0.1:8000/admin/

> Файлы миграций уже хранятся в репозитории, поэтому при обычной установке нового компьютера команда `makemigrations` не нужна. Используй её только после изменения моделей Django.

## Запуск без PostgreSQL (SQLite)

SQLite входит в стандартную библиотеку Python и отдельно устанавливать её не нужно. Чтобы использовать SQLite, открой `.env` и удали или закомментируй строку `POSTGRES_DB=journal`. При отсутствии этой переменной Django автоматически использует локальный файл `db.sqlite3`.

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
