from datetime import timedelta

from celery import shared_task
from celery.utils.time import timezone
from django.core.mail import send_mail

from config import settings
from cool_school.models import Subscription, Payment
from user.models import User


@shared_task
def send_updated_email(course):
    subscribers = Subscription.objects.get(course=course)
    send_mail(
        'Здравствуйте! С вами школа Cool-school ',
        f'Сообщаем, вам что курс на который вы подписаны был обновлён',
        settings.EMAIL_HOST_USER,
        [subscribers.user]
    )


def check_inactive_users():
    # Получение текущей даты и время
    now = timezone.now()

    # Вычисление даты месяц назад
    one_month_ago = now - timedelta(days=30)

    # Получение неактивных пользователей, которые не заходили в систему более месяца
    inactive_users = User.objects.filter(last_login__lte=one_month_ago, is_active=True)

    # Деактивация неактивных пользователей
    for user in inactive_users:
        user.is_active = False
        user.save()

    return f"{inactive_users.count()} пользователи были деактивированы."
