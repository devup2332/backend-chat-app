# Generated by Django 3.2 on 2021-05-12 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210512_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchat',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userchat',
            name='is_staff',
        ),
    ]
