from django.contrib import admin
from imgProcess.models import CommentModel,ImageModel
# Register your models here.


admin.site.register(CommentModel)
# admin.site.register(MyUser)
admin.site.register(ImageModel)