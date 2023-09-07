from django.urls import path
from .import views
# from app.views import *


urlpatterns = [
    path('<str:group_name>/', views.index),
    # path('register/', UserRegistrationView.as_view(), name='register')
]