from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title 