# Generated by Django 3.2 on 2021-05-12 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210512_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchat',
            name='name',
        ),
    ]