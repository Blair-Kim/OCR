# Generated by Django 4.2.5 on 2023-09-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20230831_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_master',
            name='user_actiavte',
            field=models.CharField(default='0', max_length=8),
        ),
    ]
