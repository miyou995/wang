
from django.urls import path, include
from .views import IndexView, AboutView, ProductsView, ProjectView,ProjectDetailView, ProjectV2View, ShopView, ShopDetailView, BlogView, BlogDetailView
urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('about/',AboutView.as_view(), name='about'),
    path('produits/',ProductsView.as_view(), name='products'),
    path('project/',ProductsView.as_view(), name='project'),
    path('ProjectDetailView/',ProjectDetailView.as_view(), name='project-detail'),
    path('project-v2/',ProjectV2View.as_view(), name='project-v2'),
    path('shop/',ShopView.as_view(), name='shop'),
    path('shop-detail/',ShopDetailView.as_view(), name='shop-detail'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('blog-detail/',BlogDetailView.as_view(), name='blog-detail'),
]
