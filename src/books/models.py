from django.db import models

from app.models import TimestampedModel


class Author(TimestampedModel):
    name = models.CharField(max_length=255)


class Book(TimestampedModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
