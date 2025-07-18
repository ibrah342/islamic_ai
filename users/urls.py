from django.urls import path
from .views import SignupView, ProtectedTestView, SignupView, ProtectedExampleView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('protected/', ProtectedTestView.as_view(), name='protected'),
    path('test/', ProtectedExampleView.as_view()),

    path('profile/', UserProfileView.as_view(), name='user_profile'),



]
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMjA3MTM0LCJpYXQiOjE3NTIyMDY4MzQsImp0aSI6IjIzMmM0OGEwNWQzOTQzMTY5MzQ4NzRhYjQ1YjMyZjc5IiwidXNlcl9pZCI6MX0.t2YK3rfbhpogDoZylNSv0CxDZcvn0_oqjyPeHt0Z2zI"

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjI5MzY4MywiaWF0IjoxNzUyMjA3MjgzLCJqdGkiOiI3NTEwMmM2ZGQyYjU0OTk2OWZhNDJiMWFiODliMzVjYSIsInVzZXJfaWQiOjF9.ZJFKSxit862QXSPMrFaMMSDjyIYbGSeojSoTRCtAIZM