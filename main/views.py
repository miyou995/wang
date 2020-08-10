from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Categorie, Produit, Reference
# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        context["produits"] = Produit.objects.all()
        context["references"] = Reference.objects.all()

        return context
    

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context


class ProductsView(TemplateView):
    template_name = "Products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context


class ProjectView(TemplateView):
    template_name = "project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context


class ProjectDetailView(TemplateView):
    template_name = "project-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context

        
class ProjectV2View(TemplateView):
    template_name = "project-v2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context

        
class ShopView(TemplateView):
    template_name = "shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context

        
class ShopDetailView(TemplateView):
    template_name = "shop-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context

        
class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context

        
class BlogDetailView(TemplateView):
    template_name = "blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        return context