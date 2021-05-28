# Generated by Django 3.2.2 on 2021-05-26 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210526_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.chat'),
        ),
    ]