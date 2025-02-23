from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class SurveyResponses(models.Model):
    answers = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.answers
