from django.contrib import admin
from imgProcess.models import CommentModel, ImageModel, UserProfileInfo
# Register your models here.

admin.site.register(CommentModel)
admin.site.register(UserProfileInfo)
admin.site.register(ImageModel)