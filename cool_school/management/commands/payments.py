from django.core.management.base import BaseCommand
from cool_school.models import Payment, User, Course, Lesson
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Загрузка данных о платежах в модель Payment'

    def handle(self, *args, **options):
        fake = Faker()

        users = []
        for _ in range(10):
            user = User.objects.create(
                email=fake.email(),
                first_name=fake.user_name(),
                last_name=fake.user_name(),
                is_staff=False,
                is_superuser=False,
                is_active=True
            )

            user.set_password('12345')
            user.save()

            users.append(user)

        courses = []
        for _ in range(10):
            course = Course.objects.create(
                title=fake.catch_phrase(),
                preview=None,
                description=fake.text(max_nb_chars=150)
            )
            courses.append(course)

        lessons = []
        for _ in range(10):
            lesson = Lesson.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(max_nb_chars=150),
                preview=None,
                video_link=fake.url()
            )
            lessons.append(lesson)

        for _ in range(10):
            user = random.choice(users)
            course = random.choice(courses)
            lesson = random.choice(lessons)

            payment = Payment.objects.create(
                user=user,
                payment_date=fake.date(),
                course=course,
                lesson=lesson,
                amount=random.uniform(10, 1000),
                payment_method=random.choice(['cash', 'transfer'])
            )

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены.'))
