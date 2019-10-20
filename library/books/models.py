from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_date = models.DateField()
    
    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    copies = models.IntegerField()
    purchase_date = models.DateField()
    created_date = models.DateField()
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
