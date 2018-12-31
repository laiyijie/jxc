from django.urls import path
from .views import *

urlpatterns = [
    path('login', UserLogin.as_view()),
    path('logout', UserLogout.as_view())
]
