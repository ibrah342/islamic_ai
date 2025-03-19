from django.db import models

# Create your models here.
class Question(models.Model):
    user_question = models.TextField()
    response = models.TextField()
    source = models.CharField(max_length=50)  # "Quran", "Hadith", "ChatGPT"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_question[:50]  # Show first 50 chars of the question
