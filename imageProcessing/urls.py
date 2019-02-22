"""imageProcessing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from imgProcess import views
from django.contrib.auth import views as djangoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url('admin/', admin.site.urls),
                  url(r'^$', views.home, name="home"),
                  url(r'', include("imgProcess.urls")),
                  url(r'^account/login/$', djangoView.login, name="login"),
                  url(r'^account/logout/$', djangoView.logout, name="logout", kwargs={"next_page": views.home}),
                  url(r'^register/$', views.register, name='register'),

                  url(r"^change_black_white$", views.change_black_white, name="change_black_white"),
                  url(r"^reset_image$", views.reset_image, name="reset_image"),
                  url(r"^change_size_of_image$", views.change_size_of_image, name="change_size_of_image"),
                  url(r"^change_contract_image$", views.change_contract_image, name="change_contract_image"),
                  url(r"^user_add_comment$", views.user_add_comment, name="user_add_comment"),
                  url(r"^follow$", views.follow, name="follow"),
                  url(r"^unfollow$", views.unfollow, name="unfollow"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
