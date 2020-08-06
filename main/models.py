from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    icon = models.ImageField(upload_to='product/')
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    def __str__(self):
        return self.name


