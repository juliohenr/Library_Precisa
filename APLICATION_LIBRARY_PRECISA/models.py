from django.db import models
from datetime import datetime


# Create your models here.

class Book_description(models.Model):

    book_name = models.CharField(max_length=200)

    synopsis = models.TextField()

    author = models.CharField(max_length=200)

    volume = models.IntegerField()

    version = models.IntegerField()

    category = models.CharField(max_length=200)

    date_insert_book = models.DateTimeField(default=datetime.now,blank=True)

    url_image = models.CharField(max_length=200)

  



    