from django.db import models

# Create your models here.

class care(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self)  ->str:
        return self.name