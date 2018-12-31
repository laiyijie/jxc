from django.urls import path
from .views import *

urlpatterns = [
    path('info', RepoAction.as_view()),
    path('all', Repos.as_view()),
    path('search', RepoSearch.as_view())
]
