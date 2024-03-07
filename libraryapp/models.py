from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
    
    def __str__(self) -> str:
        return self.title
    