import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Class of question.

    ...

    Attributes
    ----------
    question_text : CharField
        text of the question.
    pub_date : DateTimeField
        published date of question
    end_date : DateTimeField
        end date of the question

    Methods
    -------
    was_published_recently()
        check if question now published or not.

    is_published()
        check if the question is published yet.

    can_vote()
        check if the question can vote or not.

    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField(
        'date end', default=timezone.now() + datetime.timedelta(days=1))

    def __str__(self):
        """The method that will return the question text"""
        return self.question_text

    def was_published_recently(self):
        """The method that will check the question status that is published or not"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def is_published(self):
        """The method that will check the question that is published or not"""
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """The method that will check is the question can vote or not"""
        now = timezone.now()
        return self.pub_date <= now <= self.end_date


class Choice(models.Model):
    """Class of choice."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """The method that will return the choice text"""
        return self.choice_text
