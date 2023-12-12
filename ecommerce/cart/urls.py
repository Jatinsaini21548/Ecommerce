from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart', views.addtocart, name = "addtocart"),
    path('cart', views.viewcart , name= 'cart'),
    path('update-cart', views.updatecart, name = 'updatecart'),
    path('delete-cart-item', views.deletecartitem, name = "deletecartitem"), 
]