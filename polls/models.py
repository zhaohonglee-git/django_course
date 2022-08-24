import http
from django.db import models
import datetime as dt
from datetime import timedelta, datetime
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

    def __str__(self):
        print(self.pub_date)
        print(type(self.pub_date))
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = datetime.now()
        base_datetime = now - timedelta(days=3)
        base_datetime2date = datetime.date(base_datetime)
        return self.pub_date > base_datetime2date


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
