from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Catalog(models.Model):
    title= models.CharField(max_length=200,unique=True)
    image= models.CharField(max_length=1000)
    release_date = models.DateField("date published")
    genre= models.CharField(max_length=200)
    bio= models.TextField(max_length=2500)
    review =models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.title
    