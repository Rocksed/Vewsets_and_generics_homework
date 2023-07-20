from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта')
    username = models.CharField(max_length=50, verbose_name='Имя пользователя', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=25, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


