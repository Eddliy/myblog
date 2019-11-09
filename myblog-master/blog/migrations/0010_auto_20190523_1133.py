# Generated by Django 2.2.1 on 2019-05-23 11:33

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190523_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture_test',
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(default='/blog/static/blog/img/lifestyle.jpg', upload_to='my_post/images'),
        ),
    ]
