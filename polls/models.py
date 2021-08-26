from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Memant(models.Model):

    heiza = models.IntegerField(default=0)
    heiza_text = models.TextField(blank=True, null=True, max_length=100)
    heiza_answer = models.TextField(blank=True, null=True, max_length=100)
    heiza_email = models.EmailField(
        blank=False, null=False, default="nonone@none.com")

    def __str__(self):
        return self.heiza_text
