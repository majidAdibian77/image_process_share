# Generated by Django 2.0.7 on 2019-02-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgProcess', '0002_remove_userprofileinfo_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20, verbose_name='Username')),
                ('image', models.ImageField(blank=True, upload_to='user_images')),
                ('post', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]
