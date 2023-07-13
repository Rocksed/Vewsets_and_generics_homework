# Generated by Django 4.2.3 on 2023-07-13 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cool_school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cool_school.user'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cool_school.course'),
        ),
    ]