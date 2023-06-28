Проект "test_task"

Проект "test_task" является простым приложением на основе Python+Django, предназначенным для управления задачами. Приложение использует базу данных PostgreSQL и может быть развернуто в контейнере Docker для удобной установки и запуска.
Требования

Перед началом развертывания проекта у вас должны быть установлены следующие компоненты:

    Docker: Установка Docker
    Docker Compose: Установка Docker Compose
    Git (для клонирования репозитория проекта)

Развертывание

1.Клонируйте репозиторий проекта на вашу локальную машину, выполнив следующую команду:

    git clone https://github.com/Mklyd/test_task.git

2.Запустите команду docker-compose build, чтобы собрать образ и зависимости :

    docker-compose build

3.Запустите команду docker-compose up, чтобы запустить контейнеры проекта:

    docker-compose up
    
Запуск

1. Запустите команду makemigrations для создания миграций:

    docker-compose exec web python manage.py makemigrations

2.Запустите команду migrate, чтобы применить миграции :

    docker-compose exec web python manage.py migrate

Использование приложения

1. Запустите команду createsuperuser для создания администратора:

    docker-compose exec web python manage.py createsuperuser

2. Откройте веб-браузер и перейдите по адресу http://localhost:8000/admin.

3. Добавьте задачи в административной панели
4. Перейдите по адресу http://localhost:8000/tasks, для просмотра добавленных задач
