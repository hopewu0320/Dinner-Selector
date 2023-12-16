from django.db import models

# Create your models here.

class Tag(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.description
    
class Food(models.Model):
    name = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag,blank=True)
    def __str__(self) -> str:
        return self.name