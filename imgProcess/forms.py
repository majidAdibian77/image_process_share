from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from imgProcess.models import UserProfileInfo, PostModel
from django import forms


class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserEditForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic', 'bio',)
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ("image", "post",)
        widgets = {
            'post': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

