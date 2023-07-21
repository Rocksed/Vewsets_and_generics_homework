from rest_framework import status
from rest_framework.test import APITestCase

from cool_school.models import Lesson, Course
from user.models import User


class LessonTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.lesson = Lesson.objects.create(
            title='TestLesson1',
            description='Testing'

        )
        self.user = User.objects.create(
            email='test@yandex.ru',
            is_superuser=True
        )
        self.user.set_password('1234')
        self.user.save()
        response = self.client.post(
            '/api/token/',
            {
                'email': 'test@yandex.ru',
                'password': '1234'
            }
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_get_all_lessons(self):
        response = self.client.get(
            '/lesson/'

        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        response = self.client.post(
            '/lesson/create/',
            {'title': 'TestLesson2',
             'description': 'Testing',
             'video_link': 'https://yotube.com/'
             }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_lesson(self):
        response = self.client.delete(
            '/lesson/delete/3'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_lesson_retrieve(self):
        response = self.client.get(
            '/lesson/detail/5'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class SubscriptionTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.course = Course.objects.create(
            title='TestCourse',
            description='Test'
        )

        self.user = User.objects.create(
            email='test@yandex.ru',
            is_superuser=True
        )
        self.user.set_password('1234')
        self.user.save()
        response = self.client.post(
            '/api/token/',
            {
                'email': 'test@yandex.ru',
                'password': '1234'
            }
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_sub(self):
        response = self.client.post(
            '/subscription/create/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
