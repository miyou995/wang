
from django.urls import path, include
from .views import IndexView, AboutView, ProductsView, ContactView, FaqView, ProductDetailView



urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('about/',AboutView.as_view(), name='about'),
    path('produits-<slug:slug>/',ProductsView.as_view(), name='products'),
    path('produits/<slug:slug>/',ProductDetailView.as_view(), name='product-detail'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('faq/',FaqView.as_view(), name='faq'),
]
