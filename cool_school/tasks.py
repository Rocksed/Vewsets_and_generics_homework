from celery import shared_task
from django.core.mail import send_mail

from config import settings
from cool_school.models import Subscription, Payment


@shared_task
def send_updated_email(course):
    subscribers = Subscription.objects.get(course=course)
    send_mail(
        'Здравствуйте! С вами школа Cool-school ',
        f'Сообщаем, вам что курс на который вы подписаны был обновлён',
        settings.EMAIL_HOST_USER,
        [subscribers.user]
    )


def check_task():
    query = Payment.objects.filter(status='requires_confirmation')
    if query.exists():
        for q in query:
            q.status = 'succeded'
            q.save()
