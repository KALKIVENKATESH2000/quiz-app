from optparse import Option
from django.db import models


class Exam(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    carrans = models.CharField(max_length=100)

    def __str__(self):
        return self.question
