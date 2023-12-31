# Generated by Django 4.2.3 on 2023-07-13 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cool_school', '0005_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='course_or_lesson',
        ),
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cool_school.course', verbose_name='оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cool_school.lesson', verbose_name='оплаченный урок'),
        ),
    ]
