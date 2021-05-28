# Generated by Django 3.2.2 on 2021-05-26 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
        migrations.AddField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]