# Generated by Django 2.2.1 on 2019-05-20 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='url',
        ),
    ]