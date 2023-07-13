# Generated by Django 4.2.3 on 2023-07-13 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cool_school', '0004_remove_course_user_remove_lesson_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')], max_length=10, verbose_name='способ оплаты')),
                ('course_or_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cool_school.course', verbose_name='оплаченный курс или урок')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cool_school.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cool_school.user')),
            ],
        ),
    ]
