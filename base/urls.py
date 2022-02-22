from django.urls import path
from base import views
from .views import *

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('search/', SearchResultsView.as_view(), name="search"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product"),
]