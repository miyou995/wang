from django.db import models
from tinymce import models as tinymce_models
from PIL import Image

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
    image = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product/')
    image3 = models.ImageField(upload_to='product/')
    image4 = models.ImageField(upload_to='product/')
    image5 = models.ImageField(upload_to='product/')
    fiche = models.ImageField(upload_to='product/fiche/', blank=True)
    fiche2 = models.ImageField(upload_to='product/fiche/', blank=True)
    fiche3 = models.ImageField(upload_to='product/fiche/', blank=True)
    actif = models.BooleanField(default=True)
    content = tinymce_models.HTMLField(blank=True)
    
    def __str__(self):
        return self.name

#a revoir pour resizer toutes les images 
    def save(self, *args, **kwargs):
        super(Produit, self).save(*args, **kwargs)
        image = self.image.path
        image2 = self.image2.path
        image3 = self.image3.path
        image4 = self.image4.path
        # images = ['image', 'image2', 'image3', 'image4', 'image5']
        images = [image, image2, image3, image4]
        for img in images:
            size = 761, 509
            image = Image.open(img)
            image.thumbnail(size)
            image.save(img)


            # reel= (700, 500)
            # final = img.resize(reel)
            # final.save(self.image2.path)


class Reference(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='ref/')
    
    def __str__(self):
        return self.name

class Question(models.Model):
    QUESTION_LIST = [
        ('PP', 'A propos des produits'),
        ('SA', 'Service après-vente'),
        ('AU', 'A propos de l\'usine - visite'),
    ]
    propos = models.CharField(max_length=2, choices=QUESTION_LIST)
    question = models.CharField(max_length=200 )
    reponse = models.CharField(max_length=200, blank=True)
    content = tinymce_models.HTMLField(blank=True)

    def __str__(self):
        return self.question
    