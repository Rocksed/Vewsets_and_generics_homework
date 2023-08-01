from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
from django_celery_beat.models import PeriodicTask

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('Vewsets_and_generics_homework')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Выполнение задачи Celery на каждый день в  3:00 AM
    PeriodicTask.objects.get_or_create(
        name='Задача проверки неактивных пользователей',
        task='cool_school.tasks.check_inactive_users',
        interval=timedelta(days=1),
        start_time='03:00',  # Установка времени начала выполнения задачи
    )
