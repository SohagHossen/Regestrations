from django.db import models

# Create your models here.
class Vegetable(models.Model):
  rec_name = models.CharField(max_length=50)
  rec_price =models.IntegerField()
  rec_dis= models.TextField()
  rec_image = models.ImageField(upload_to='static/images/')

