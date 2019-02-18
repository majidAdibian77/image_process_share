from datetime import datetime
# from time import timezone

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

#
# class FollowUsers(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
#     bio = models.TextField(max_length=100, blank=True, default="Bio")
#     profile_pic = models.ImageField(upload_to='profile_users', blank=True, default="")
#
#     def __str__(self):
#         return self.user.username


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, blank=True, default="Bio")
    profile_pic = models.ImageField(upload_to='profile_users', blank=True)
    following = models.OneToOneField(User, related_name="following", on_delete=models.CASCADE, default="")
    followers = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.user.username


# class ImageModel(models.Model):
#     username = models.CharField(max_length=20, verbose_name="Username", default="")
#     image = models.ImageField(upload_to='user_images', blank=True)
#
#     def __str__(self):
#         return self.username


#
# class LogInModel(models.Model):
#     user_name = models.CharField(max_length=20, verbose_name="User Name")
#     password = models.CharField(max_length=20, verbose_name="password")


class PostModel(models.Model):
    username = models.CharField(max_length=20, unique=False, verbose_name="Username", default="")
    image = models.ImageField(upload_to='user_images', blank=True)
    post = models.TextField(max_length=100, blank=True)
    post_time = models.DateTimeField(default=datetime.now, blank=True)

    def set_post_time(self):
        self.post_time = datetime.now()
        self.save()

    def __str__(self):
        return self.username


class CommentPostModel(models.Model):
    profile_user = models.OneToOneField(UserProfileInfo, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Text")
    comment_time = models.DateTimeField(default=datetime.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

    # username = models.CharField(max_length=20, verbose_name="Username", default="")
    # image = models.ImageField(upload_to='user_images')
