import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



    def __str__(self):
        """
        It's important to add __str__() methods to your models,
        not only for your own convenience when dealing with the interactive prompt,
        but also because objects' representations are used throughout
        Django's automatically-generated admin.
        """
        return self.question_text

    # the @admin.display is a decorator 
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        # Fix bug
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

