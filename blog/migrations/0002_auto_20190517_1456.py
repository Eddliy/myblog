# Generated by Django 2.2.1 on 2019-05-17 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
