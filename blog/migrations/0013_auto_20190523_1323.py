# Generated by Django 2.2.1 on 2019-05-23 13:23

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190523_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='/my_post/images/selfie.jpg', upload_to='my_post/images'),
        ),
    ]