from django.db import models

# Create your models here.
class Book(models.Model):#creating a table
    author=models.CharField(max_length=50,null=True)#these are the columns
    book_name=models.CharField(max_length=50,null=True)
    isbn=models.IntegerField(null=True)
