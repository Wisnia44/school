from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    UserLogoutView,
    UserChangePassword,
    IndexView,
)

#app_name = ''
urlpatterns = [
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user-change-password/', UserChangePassword.as_view(), name='change-password'),
    path('', IndexView.as_view(), name='index'),
    url('^', include('django.contrib.auth.urls')),
]
