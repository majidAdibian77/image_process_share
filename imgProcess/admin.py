from django.contrib import admin
from imgProcess.models import CommentModel, PostModel, UserProfileInfo, CommentPostModel, FollowerUsers, FollowingUsers
# Register your models here.

admin.site.register(CommentModel)
admin.site.register(UserProfileInfo)
admin.site.register(PostModel)
admin.site.register(CommentPostModel)
admin.site.register(FollowerUsers)
admin.site.register(FollowingUsers)