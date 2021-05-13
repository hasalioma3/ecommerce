from django.db import models

# Create your models here.

class Pics(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name="picture"
        verbose_name_plural="pictures"

    def __str__(self):
        return self.name
    