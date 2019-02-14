from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class CommentModel(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name")
    text = models.TextField(verbose_name="Text")
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()


# class SignInModel(models.Model):
#     name = models.CharField(max_length=20, verbose_name="Name")
#     user_name = models.CharField(max_length=20, verbose_name="Username")
#     password = models.CharField(max_length=20, verbose_name="password")
#     email = models.EmailField()
#

# class MyUser(User):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_users', blank=True)

    def __str__(self):
        return self.user.username


class ImageModel(models.Model):
    username = models.CharField(max_length=20, verbose_name="Username", default="")
    image = models.ImageField(upload_to='user_images', blank=True)

    def __str__(self):
        return self.username
    # username = models.CharField(max_length=20, verbose_name="Username", default="")
    # image = models.ImageField(upload_to='user_images')

#
# class LogInModel(models.Model):
#     user_name = models.CharField(max_length=20, verbose_name="User Name")
#     password = models.CharField(max_length=20, verbose_name="password")
