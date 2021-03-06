from django.conf.urls import url
from imgProcess import views

urlpatterns = [
    # url(r'^sign_in/$', views.sign_in, name="sign_in"),
    # url(r'^log_in/$', views.log_in, name="log_in"),

    url(r'^upload_image/$', views.upload_image, name="upload_image"),
    url(r'^change_image/$', views.change_image, name="change_image"),
    url(r'^profile_page/(?P<pk>\d+)$', views.profile_page, name="profile_page"),
    url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^delete_post/(?P<pk>\d+)$', views.delete_post, name="delete_post"),
]