# Generated by Django 4.2.3 on 2023-07-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cool_school', '0006_remove_payment_course_or_lesson_payment_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя пользователя'),
        ),
    ]