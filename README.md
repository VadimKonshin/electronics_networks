В данном проекте мы разработали онлайн платформу-торговой сети электроники.

Технологии которые были применены в данном проекте:

    Python
    Django
    DRF
    
    PostgreSQL
    
Работа с приложением:

    - Клонируем приложение из github-a.
    - Активируем виртуально окружение.
    - Устанавливаем зависимости pip install -r requirements.txt либо если у вас poetry то poetry install
    - Создаем и вносим данные в файл .env, все данные указанные в .env.sample
    - Создаем миграции python3 manage.py malemigrations и применяем их python3 manage.py migrate
    - Запускаем django приложение командой python3 manage.py runserver. Если у вас poetry то используем команду python manage.py runserver
