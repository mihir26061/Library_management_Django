from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "my_books"


class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'admin'
