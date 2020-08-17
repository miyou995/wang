from django.contrib import admin

# Register your models here.
from .models import Categorie, Produit, Reference

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Produit)
class CategorieAdmin(CategorieAdmin):
    list_display = ('id', 'name', 'categorie','actif','page_accueil')
    list_display_links = ('id', 'name', 'categorie')
    list_filter = ('id', 'name', 'categorie',)
    list_editable = ['actif','page_accueil']


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name')
