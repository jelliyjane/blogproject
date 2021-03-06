from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title