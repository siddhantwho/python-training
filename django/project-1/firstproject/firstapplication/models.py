from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=10)
    id_number = models.IntegerField()
    contact = models.TextField()
    address= models.TextField()

    def __str__(self):
        return self.name