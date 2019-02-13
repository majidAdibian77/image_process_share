import numpy as np
from PIL import Image, ImageEnhance
from django.http import JsonResponse

from django.shortcuts import render, redirect
from imgProcess.forms import CommentForm, Upload
from imgProcess.models import CommentModel, ImageModel
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


def delete_image(request):
    img = ImageModel.objects.filter(username=request.user.username)
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
    comments = CommentModel.objects.all()
    hash["comments"] = comments
    return render(request, "imgProcess/home.html", hash)


def add_comment(request):
    delete_image(request)
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
    delete_image(request)
    upload_form = Upload()
    error = ""
    if request.method == "POST":
        upload_form = Upload(request.POST, request.FILES)
        # upload_form.set_user(request.user.username)
        if upload_form.is_valid():
            if upload_form.cleaned_data["username"] != request.user.username:
                error = "Your username is false"
            else:
                upload_form.save()

                return redirect("change_image")
    return render(request, "uploadImage.html", {"form": upload_form, "error": error})


@login_required
def change_image(request):
    hash = {}
    images = ImageModel.objects.filter(username=request.user.username)
    # for img in images:
    #     size = 500, 400
    #     im = Image.open(img.image.url[1:])
    #     im.thumbnail(size, Image.ANTIALIAS)
    #     im.save(img.image.url[1:])
    hash["all_image"] = images
    return render(request, "change_image.html", hash)


def change_black_white(request):
    image_url = request.GET.get("image_url", None)
    image_file = Image.open(image_url[1:])  # open colour image
    image_file = image_file.convert('L')  # convert image to black and white
    new_image_url = image_url[:image_url.rfind('.')] + "_new1" + image_url[image_url.rfind('.'):]
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
    img.thumbnail(size, Image.ANTIALIAS)
    new_image_url = image_url[:image_url.rfind('.')] + "_new" + image_url[image_url.rfind('.'):]
    img.save(new_image_url[1:])
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
