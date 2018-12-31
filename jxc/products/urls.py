from django.urls import path
from .views import *

urlpatterns = [
    path('info', ProductAction.as_view()),
    path('all', ProductAll.as_view()),
    path('search', ProductSearch.as_view())
]
