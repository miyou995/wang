from django.contrib import admin

# Register your models here.
from .models import Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name',)
    search_fields = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
