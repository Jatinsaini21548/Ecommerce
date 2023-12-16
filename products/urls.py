from django.urls import path
from . import views

urlpatterns = [
    path('collections', views.collections, name="collections"),
    path('collections_view/<int:id>', views.collectionsview, name="collectionsview"),
    path('productview/<int:id>', views.productview, name="productview"),
]
