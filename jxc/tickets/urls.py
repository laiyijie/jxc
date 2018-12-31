from django.urls import path
from .views import *

urlpatterns = [
    path('customer', GetTickets.as_view()),

]
