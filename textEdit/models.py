from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ Basic model for a Topic
    Return:
        title (str): The title of the topic.
    """
    title = models.CharField(max_length=100)
    # text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Entry(models.Model):
    """ Basic model for an entry in a Topic
    Return:
        text(str): The text with a max length of 50
    """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'
