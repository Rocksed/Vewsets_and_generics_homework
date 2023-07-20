# Generated by Django 4.2.3 on 2023-07-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя пользователя')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Аватар')),
                ('city', models.CharField(blank=True, max_length=25, null=True, verbose_name='Город')),
            ],
        ),
    ]