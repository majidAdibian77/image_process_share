from django.conf.urls import url
from imgProcess import views

urlpatterns = [
    # url(r'^sign_in/$', views.sign_in, name="sign_in"),
    # url(r'^log_in/$', views.log_in, name="log_in"),

    url(r"^add_comment$", views.add_comment, name="add_comment"),
    url(r'^upload_image/$', views.upload_image, name="upload_image"),
    url(r'^change_image/$', views.change_image, name="change_image"),
]