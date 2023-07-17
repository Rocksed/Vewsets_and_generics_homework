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


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название урока')
    description = models.CharField(max_length=150, verbose_name='описание урока')
    preview = models.ImageField(upload_to='media_lesson/', verbose_name='картинка урока', **NULLABLE)
    video_link = models.CharField(max_length=50, verbose_name='ссылка на урок')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Course(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    title = models.CharField(max_length=50, verbose_name='название курса')
    preview = models.ImageField(upload_to='media/', verbose_name='картинка к курсу', **NULLABLE)
    description = models.CharField(max_length=150, verbose_name='описание курса')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс',
                               **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='способ оплаты',
                                      max_length=10,
                                      choices=[
                                          ('cash', 'Наличные'),
                                          ('transfer', 'Перевод на счет')
                                      ]
                                      )

    def __str__(self):
        return f'{self.user} - {self.payment_date}'
