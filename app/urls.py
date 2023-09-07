from django.urls import path,include
from .import views
# from app.views import *


urlpatterns = [
    path('<str:group_name>/', views.index),
    path('acc/', include('account.urls'))
    # path('register/', UserRegistrationView.as_view(), name='register')
]