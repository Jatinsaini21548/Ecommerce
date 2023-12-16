from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart', views.addtocart, name = "addtocart"),
    path('cart', views.viewcart , name= 'cart'),
    path('update-cart', views.update_cart, name = 'update_cart'),
    path('delete-cart-item/<int:id>', views.deletecartitem, name = 'deletecartitem'),
    path('checkout', views.checkout , name='checkout'),
    path('payment', views.payment , name = 'payment'),
    path('address_select', views.address_select , name = 'address_select'),
]