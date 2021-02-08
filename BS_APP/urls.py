from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('users/',user),
    path('transfer/<int:pk>',transfer),
    path('add_transfer/',add_transfer),
    path('history/',history)
]