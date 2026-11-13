# Электронный журнал

Учебный проект электронного журнала на **Django 5.1.4**, Django REST Framework и **PostgreSQL**. В проекте пять приложений: `accounts`, `catalog`, `clients`, `orders`, `reports`.

## Функциональные модули

- `accounts` — пользователи, роли и авторизация.
- `catalog` — учебные годы, классы и предметы.
- `clients` — ученики и контактные представители.
- `orders` — уроки, оценки и посещаемость.
- `reports` — сводные показатели и API-отчёты.

API реализован на Django REST Framework. Используются сессионная и Basic-аутентификация; JWT не требуется. PostgreSQL — база данных проекта.

## Требования

- Windows 10/11 (инструкции ниже — PowerShell)
- Python 3.12
- PostgreSQL 16 или новее

## Установка и запуск

1. Откройте папку проекта в VS Code.
2. Создайте и активируйте виртуальное окружение:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Создайте локальный файл настроек и задайте параметры PostgreSQL:

```powershell
Copy-Item .env.example .env
```

Укажите пароль в `POSTGRES_PASSWORD`. Файл `.env` содержит локальные секреты и не должен попадать в Git.

4. Создайте базу данных в PostgreSQL (например, через pgAdmin или psql):

```sql
CREATE DATABASE electronic_journal;
```

5. Выполните миграции и проверки, затем создайте администратора:

```powershell
python manage.py check
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runserver
```

6. Откройте `http://127.0.0.1:8000/`. Админ-панель доступна по адресу `http://127.0.0.1:8000/admin/`, API — `http://127.0.0.1:8000/api/`, сводный отчёт — `http://127.0.0.1:8000/api/reports/summary/`.

## Миграции и существующие базы

Миграции включены в проект. Миграция `accounts.0003` проверяет наличие столбцов `middle_name` и `phone` и добавляет только отсутствующие. Это позволяет запускать проект как на новой базе, так и на базе, где начальная миграция уже была применена без этих столбцов. Удалять базу данных или помечать миграции как выполненные вручную не требуется.

## Состав репозитория и безопасность

В репозитории хранится исходный код, миграции, шаблоны и файл `.env.example`. Виртуальное окружение `.venv`, локальный `.env`, кэш Python и пользовательские файлы не включаются.
