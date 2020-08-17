from django.db import models
from tinymce import models as tinymce_models
# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    icon = models.ImageField(upload_to='product/')
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Produit(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    definition = models.TextField()
    presentation = models.TextField()
    page_accueil = models.BooleanField(default= False, verbose_name='Page d\'accueil')
    image = models.ImageField(upload_to='product/', blank=True)
    image2 = models.ImageField(upload_to='product/', blank=True)
    image3 = models.ImageField(upload_to='product/', blank=True)
    image4 = models.ImageField(upload_to='product/', blank=True)
    image5 = models.ImageField(upload_to='product/', blank=True)
    fiche = models.ImageField(upload_to='product/fiche/')
    actif = models.BooleanField(default=True)
    content = tinymce_models.HTMLField()

class Reference(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='ref/')
    
    def __str__(self):
        return self.name