from django.urls import path, include
from .views import UserDetailView

urlpatterns = [
	path('user/profile/',UserDetailView.as_view(), name='user-profile')
]
