from django.contrib import admin
from imgProcess.models import CommentModel, PostModel, UserProfileInfo, CommentPostModel
# Register your models here.

admin.site.register(CommentModel)
admin.site.register(UserProfileInfo)
admin.site.register(PostModel)
admin.site.register(CommentPostModel)