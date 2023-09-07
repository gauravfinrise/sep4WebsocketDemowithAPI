from django.urls import path
from .views import UserRegistrationAPIView, LoginView, login_page, logout_view
# UserLoginView,

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('login-page/', login_page, name='login_page'),
    path('logout/', logout_view, name='logout'),
    # path('login/', UserLoginView.as_view(), name='your-login-view-name'),
]