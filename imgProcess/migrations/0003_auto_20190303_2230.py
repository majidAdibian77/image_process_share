# Generated by Django 2.0.7 on 2019-03-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgProcess', '0002_auto_20190223_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='server_images/user_image.jpg', upload_to='profile_users'),
        ),
    ]