# Generated by Django 2.0.7 on 2019-02-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgProcess', '0003_auto_20190215_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='bio',
            field=models.TextField(blank=True, default='Bio', max_length=100),
        ),
    ]
