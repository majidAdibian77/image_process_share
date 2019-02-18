from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from imgProcess.models import CommentModel, UserProfileInfo, PostModel
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

class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic', 'bio',)
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


# class Upload(forms.ModelForm):
#     class Meta:
#         model = ImageModel
#         fields = ("image",)


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ("image", "post",)
        widgets = {
            'post': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

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
