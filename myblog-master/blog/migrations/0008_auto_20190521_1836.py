# Generated by Django 2.2.1 on 2019-05-21 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190521_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time']},
        ),
    ]
