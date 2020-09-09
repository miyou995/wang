from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView
from .models import Categorie, Produit, Reference, Question
from .forms import ContactForm
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
        context["produits"] = Produit.objects.all()

        return context


class ProductsView(ListView):
    template_name = "Products.html"
    model = Produit
    context_object_name = "categorie"

    def get_queryset(self):
        self.categorie = get_object_or_404(Categorie, slug=self.kwargs['slug'])
        return self.categorie


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        context["categorie"] = self.categorie
        context["produits"] = Produit.objects.all()

        context['produitsF'] = Produit.objects.filter(categorie=self.categorie)
        return context

class ProductDetailView(DetailView):
    template_name = "produit_detail.html"
    context_object_name = 'produit'
    model = Produit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icons"] = Categorie.objects.all()
        context["produits"] = Produit.objects.all()

        return context


class FaqView(TemplateView):
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produits"] = Produit.objects.all()
        context["icons"] = Categorie.objects.all()
        context["q1"] = Question.objects.filter(propos='PP')
        context["q2"] = Question.objects.filter(propos='SA')
        context["q3"] = Question.objects.filter(propos='AU')

        return context

        
class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produits"] = Produit.objects.all()
        context["icons"] = Categorie.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
    
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            honeypot = form.cleaned_data['honeypot']

            body = 'Nom: {} \n email: {} \n Phone:{} \n Sujet: {} \n Message: {}' .format(name, email, phone, subject, message)
            mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'inter.taki@gmail.com', ['inter-95@hotmail.fr']) 
            mail.send()
            messages.success(request, 'Votre message a bien été envoyer')
        return redirect('/contact')