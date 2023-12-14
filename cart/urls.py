from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart', views.addtocart, name = "addtocart"),
    path('cart', views.viewcart , name= 'cart'),
    path('update-cart<int:id>', views.update_cart, name = 'update_cart'),
    path('delete-cart-item/<int:id>', views.deletecartitem, name = "deletecartitem"), 
]