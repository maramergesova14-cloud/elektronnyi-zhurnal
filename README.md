# Электронный журнал

Учебный проект на Django REST Framework для учёта учеников, школьных предметов, оценок и посещаемости.

## Возможности

- список и управление учениками;
- список и управление предметами;
- добавление оценок ученикам;
- учёт посещаемости;
- REST API с операциями GET, POST, PATCH и DELETE;
- административная панель Django.

## Технологии

- Python
- Django
- Django REST Framework
- PostgreSQL (или SQLite для быстрого локального запуска)

## Запуск проекта

1. Установи Python 3.11 или новее.
2. Создай виртуальное окружение:

   ```bash
   python -m venv venv
   ```

   Windows: `venv\\Scripts\\activate`

   macOS/Linux: `source venv/bin/activate`

3. Установи зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Если PostgreSQL ещё не настроен, можно запустить проект на SQLite: не задавай переменную `POSTGRES_DB`. Для PostgreSQL скопируй `.env.example` в `.env`, заполни параметры базы и экспортируй переменные окружения перед запуском.
5. Создай таблицы и администратора:

   ```bash
   python manage.py makemigrations journal
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Запусти сервер:

   ```bash
   python manage.py runserver
   ```

API: http://127.0.0.1:8000/api/  
Административная панель: http://127.0.0.1:8000/admin/

## API endpoints

| Метод | URL | Назначение |
|---|---|---|
| GET | `/api/students/` | Получить список учеников |
| POST | `/api/students/` | Добавить ученика |
| GET | `/api/students/1/` | Получить ученика по ID |
| PATCH | `/api/students/1/` | Изменить часть данных ученика |
| DELETE | `/api/students/1/` | Удалить ученика |
| GET / POST | `/api/subjects/` | Просмотр и добавление предметов |
| GET / POST | `/api/grades/` | Просмотр и добавление оценок |
| GET / POST | `/api/attendance/` | Просмотр и добавление посещаемости |

Все ресурсы также поддерживают изменение и удаление отдельной записи.

## Примеры API Requests

Для примеров используется Postman или другое приложение для отправки HTTP-запросов. Базовый адрес: `http://127.0.0.1:8000`.

### 1. GET — получить учеников

- Method: `GET`
- URL: `http://127.0.0.1:8000/api/students/`

### 2. POST — добавить ученика

- Method: `POST`
- URL: `http://127.0.0.1:8000/api/students/`
- Body → raw → JSON:

```json
{
  "first_name": "Анна",
  "last_name": "Иванова",
  "class_name": "9А",
  "email": "anna@example.com"
}
```

### 3. PATCH — изменить класс ученика

- Method: `PATCH`
- URL: `http://127.0.0.1:8000/api/students/1/`
- Body → raw → JSON:

```json
{
  "class_name": "9Б"
}
```

### 4. DELETE — удалить ученика

- Method: `DELETE`
- URL: `http://127.0.0.1:8000/api/students/1/`

Для POST/PATCH выбери `Content-Type: application/json`. Авторизация в этом учебном варианте не настроена; токены не используются.

## Структура проекта

```text
config/       настройки и URL проекта
journal/      модели, сериализаторы, представления и маршруты API
manage.py     команды Django
requirements.txt
.env.example
README.md
```
