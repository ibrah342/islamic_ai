from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question
import json

@csrf_exempt  # This disables CSRF protection for this view
def ask_question(request):
    if request.method == "GET":
        return JsonResponse({"message": "Send a POST request with a question."})

    if request.method == "POST":
        data = json.loads(request.body)
        user_question = data.get("question")

        # TODO: Connect to Quran, Hadith, and ChatGPT APIs
        response = "This is a placeholder answer."

        # Save the question and response in the database
        question = Question.objects.create(
            user_question=user_question,
            response=response,
            source="ChatGPT"
        )

        return JsonResponse({"question": user_question, "answer": response})
