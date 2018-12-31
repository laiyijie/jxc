from django.urls import path
from .views import *

urlpatterns = [
    path('info', CustomerAction.as_view()),
    path('all', Customers.as_view()),
    path('search', CustomerSearch.as_view())
]
