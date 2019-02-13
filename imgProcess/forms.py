from imgProcess.models import CommentModel, ImageModel
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ("name", "text")

#
# class SignInForm(forms.ModelForm):
#     class Meta:
#         model = SignInModel
#         fields = "__all__"
#         widgets = {
#             "password": forms.PasswordInput(),
#         }


# class LogInForm(forms.ModelForm):
#     class Meta:
#         model = SignInModel
#         fields = ("user_name", "password")
#         widgets = {
#             "password": forms.PasswordInput(),
#         }


class Upload(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ["image", "username"]

    # def __init__(self, *args, **kwargs):
    #     self.username = kwargs.pop('username')
    #     super(Upload, self).__init__(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     self.instance.organizer = self.organizer
    #     upload = super(Upload, self).save(*args, **kwargs)
    #     return upload
    #
    # def set_user(self, un):
    #     self.username = un
