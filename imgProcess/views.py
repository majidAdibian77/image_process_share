import numpy as np
from PIL import Image, ImageEnhance
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from imgProcess.forms import CommentForm, PostForm, UserForm, UserProfileInfoForm
from imgProcess.models import CommentModel, UserProfileInfo, PostModel
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from imageProcessing import settings
import os


# Create your views here.

# class Home(TemplateView, ListView):
#     template_name = "home.html"
#     model = CommentModel
#

class ImageUpload(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    redirect_field_name = "imgProcess/change_image.html"
    template_name = "uploadImage.html"


class CommentFormView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "imgProcess/home.html"
    form_class = CommentForm
    model = CommentModel


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            #
            # or we can get user in other way:
            # id = request.user.id
            # user = User.objects.get(pk = id)
            #
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            auth_user = authenticate(username=user_form.cleaned_data.get('username'),
                                     password=user_form.cleaned_data.get('password1'))
            login(request, auth_user)
            return redirect("profile_page", pk= user.id)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, "registration/register.html",
                  {'user_form': user_form,
                   'profile_form': profile_form})


def delete_image(request):
    img = PostModel.objects.filter(username=request.user.username)
    for m in img.all():
        path = m.image.url[1:]
        if os.path.exists(path):
            os.remove(path)
        path2 = path[:path.rfind('.')] + "_new1" + path[path.rfind('.'):]
        if os.path.exists(path2):
            os.remove(path2)
        path3 = path[:path.rfind('.')] + "_new2" + path[path.rfind('.'):]
        if os.path.exists(path3):
            os.remove(path3)

    img.delete()


def home(request):
    delete_image(request)
    hash = {}
    users = UserProfileInfo.objects.all()
    hash["users"] = users
    return render(request, "imgProcess/home.html", hash)


def add_comment(request):
    # delete_image(request)
    hash = {}
    comment_form = CommentForm()
    hash["comment_form"] = comment_form
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if (request.user.is_authenticated):
                comment_form.save()
                return redirect("home")
    return render(request, "imgProcess/addComment.html", hash)


@login_required
def upload_image(request):
    # delete_image(request)
    upload_form = PostForm()
    error = ""
    if request.method == "POST":
        upload_form = PostForm(data=request.POST)
        if upload_form.is_valid():
            image_form = upload_form.save(commit=False)
            image_form.username = request.user.username
            if 'image' in request.FILES:
                image_form.image = request.FILES['image']
                image_form.save()
                return redirect("change_image")
        error = "There is a problem in uploading!!"
    #     upload_form = Upload(request.POST, request.FILES)
    #     # upload_form.set_user(request.user.username)
    #     if upload_form.is_valid():
    #         if upload_form.cleaned_data["username"] != request.user.username:
    #             error = "Your username is false"
    #         else:
    #             upload_form.save()
    #
    #             return redirect("change_image")
    return render(request, "uploadImage.html", {"form": upload_form, "error": error})


@login_required
def change_image(request):
    hash = {}
    images = PostModel.objects.filter(username=request.user.username)
    hash["all_image"] = images

    path = ""
    for temp in images:
        path = temp.image.url
    img = Image.open(path[1:])
    width = img.size[0]
    height = img.size[1]
    if width > 500:
        width = 500
    elif width < 200:
        width = 200
    if height > 600:
        height = 600
    elif height < 300:
        height = 300
    size = (width, height)
    temp_img = img.resize(size, Image.ANTIALIAS)
    temp_img.save(path[1:])
    return render(request, "change_image.html", hash)


def change_black_white(request):
    general_image_url = request.GET.get("general_image_url", None)
    new_image_url = request.GET.get("new_image_url", None)
    image_file = Image.open(new_image_url[1:])  # open colour image
    image_file = image_file.convert('L')  # convert image to black and white

    # if general_image_url == new_image_url:
    #     image_url = general_image_url
    #     new_image_url = image_url[:image_url.rfind('.')] + "_new1" + image_url[image_url.rfind('.'):]
    # else:
    #     image_url = new_image_url
    #     path = general_image_url[:general_image_url.rfind('.')] + "_new1" + general_image_url[
    #                                                                         general_image_url.rfind('.'):]
    #     if new_image_url == path:
    #         os.remove(path[1:])
    #         new_image_url = general_image_url[:general_image_url.rfind('.')] + "_new2" + general_image_url[
    #                                                                                      general_image_url.rfind('.'):]
    new_image_url1 = general_image_url[:general_image_url.rfind('.')] + "_new1" + general_image_url[
                                                                                  general_image_url.rfind('.'):]
    new_image_url2 = general_image_url[:general_image_url.rfind('.')] + "_new2" + general_image_url[
                                                                                  general_image_url.rfind('.'):]
    if os.path.exists(new_image_url1[1:]):
        os.remove(new_image_url1[1:])
        new_image_url = new_image_url2
    else:
        if os.path.exists(new_image_url2[1:]):
            os.remove(new_image_url2[1:])
        new_image_url = new_image_url1
    image_file.save(new_image_url[1:])
    data = {
        "newImage_url": new_image_url
    }
    return JsonResponse(data)


def reset_image(request):
    image_url = request.GET.get("image_url", None)
    path = image_url[1:]
    os.remove(path=path)
    new_image_url = image_url[:(image_url.rfind('_'))] + image_url[(image_url.rfind('.')):]
    data = {
        "newImage_url": new_image_url
    }
    return JsonResponse(data)


def change_size_of_image(request):
    image_url = request.GET.get("image_url", None)
    width = request.GET.get("width", None)
    height = request.GET.get("height", None)
    size = int(width), int(height)
    img = Image.open(image_url[1:])
    temp_img = img.resize(size, Image.ANTIALIAS)
    new_image_url1 = image_url[:image_url.rfind('.')] + "_new1" + image_url[image_url.rfind('.'):]
    new_image_url2 = image_url[:image_url.rfind('.')] + "_new2" + image_url[image_url.rfind('.'):]
    if os.path.exists(new_image_url1[1:]):
        os.remove(new_image_url1[1:])
        new_image_url = new_image_url2
    else:
        if os.path.exists(new_image_url2[1:]):
            os.remove(new_image_url2[1:])
        new_image_url = new_image_url1
    temp_img.save(new_image_url[1:])
    data = {
        "newImage_url": new_image_url
    }
    return JsonResponse(data)


def change_contract_image(request):
    image_url = request.GET.get("image_url", None)
    factor = float(request.GET.get("factor", None))
    image = Image.open(image_url[1:])
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    new_image_url1 = image_url[:image_url.rfind('.')] + "_new1" + image_url[image_url.rfind('.'):]
    new_image_url2 = image_url[:image_url.rfind('.')] + "_new2" + image_url[image_url.rfind('.'):]
    if os.path.exists(new_image_url1[1:]):
        os.remove(new_image_url1[1:])
        new_image_url = new_image_url2
    else:
        if os.path.exists(new_image_url2[1:]):
            os.remove(new_image_url2[1:])
        new_image_url = new_image_url1

    out.save(new_image_url[1:])
    data = {
        "newImage_url": new_image_url,
    }
    return JsonResponse(data)


# def add_post(request):
#     general_image_url = request.GET.get("general_image_url", None)
#     new_image_url = request.GET.get("new_image_url", None)
#     user_post = request.GET.get("post", None)
#     if general_image_url == new_image_url:
#         image_url = general_image_url
#     else:
#         image_url = new_image_url
#         os.remove(general_image_url)
#     images = PostModel.objects.filter(username=request.user.username)
#     post_img = object()
#     for img in images.all():
#         img.image.url = image_url
#         img.save()
#         post_img = img
#         break
#     Post = PostModel()
#     Post.username = request.user.username
#     Post.image = post_img
#     Post.post = user_post
#     Post.save()
#     data={
#         "successful": True
#     }
#     return JsonResponse(data)


def profile_page(request, pk):
    if pk:
        user = User.objects.get(pk = pk)
    else:
        user = request.user
    user_info = UserProfileInfo.objects.filter(user=user)
    user_posts = PostModel.objects.filter(username=user.username)
    path = ""
    for temp in user_posts:
        path = temp.image.url
        break

    path = path[1:]
    new_path1 = path[:path.rfind('.')] + "_new1" + path[path.rfind('.'):]
    new_path2 = path[:path.rfind('.')] + "_new2" + path[path.rfind('.'):]
    if os.path.exists(new_path1):
        os.remove(path)
        os.renames(new_path1, path)
    if os.path.exists(new_path2):
        os.remove(path)
        os.renames(new_path2, path)

    return render(request, "profile_page.html", {"user_info": user_info, "user_posts": user_posts})

# def log_in(request):
#     # global hash
#     hash = {}
#     hash["log_in_form"] = LogInForm()
#     hash["user_pass"] = True
#     if request.method == "POST":
#         log_in_form = LogInForm(request.POST)
#         if log_in_form.is_valid():
#             check = False
#             name = ""
#             for user in SignInModel.objects.all():
#                 if log_in_form.user_name == user.user_name and log_in_form.password == user.password:
#                     check = True
#                     name = user.name
#                     break
#             if check:
#                 hash["user"] = name
#                 return redirect("home")
#         hash["user_pass"] = False
#     return render(request, "imgProcess/login.html", hash)
#

# def sign_in(request):
#     global hash
#     hash["sign_in_form"] = SignInForm()
#     if request.method == "POST":
#         sign_in_form = SignInForm(request.POST)
#         if sign_in_form.is_valid():
#             check = True
#             name = ""
#             for user in SignInModel.objects.all():
#                 if sign_in_form.user_name == user.user_name:
#                     check = False
#                     name = user.name
#                     break
#             if check:
#                 hash["user"] = name
#                 return redirect("home")
#         hash["user_pass"] = False
#     return render(request, "imgProcess/signin.html", hash)
#
