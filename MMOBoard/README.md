Достка объявлений MMORPG Board - D16

Установка необходимых библиотек:
# pip install django-bootstrap4
# pip install django-allauth
# pip install django-ckeditor
# pip install celery
# pip install redis
Установить сервер redis на локальной машине (в зависимости от типа ОС)
# pip install -U "celery[redis]"
# celery -A MMORPG_board worker -l INFO