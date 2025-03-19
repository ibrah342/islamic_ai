from django.urls import path
from .views import ask_question  # Ensure views.py has this function

urlpatterns = [
    path("ask/", ask_question, name="ask_question"),  # ✅ Correct URL
]
