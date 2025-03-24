from django.urls import path
from .views import register, login, get_user, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('user/', get_user, name='get_user'),
    path('logout/', logout, name='logout'),
]
