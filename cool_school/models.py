from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=25, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название курса')
    preview = models.ImageField(upload_to='media/', verbose_name='картинка к курсу')
    description = models.CharField(max_length=150, verbose_name='описание курса')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название урока')
    description = models.CharField(max_length=150, verbose_name='описание урока')
    preview = models.ImageField(upload_to='media_lesson/', verbose_name='картинка урока')
    video_link = models.CharField(max_length=50, verbose_name='ссылка на урок')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
