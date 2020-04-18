from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    data = models.DateTimeField
