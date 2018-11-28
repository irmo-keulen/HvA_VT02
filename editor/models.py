from django.db import models
from tinymce.models import HTMLField


class MyModel(models.Model):
    content = HTMLField()
