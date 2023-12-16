from django.shortcuts import render
from store.views import *
from store.models import *

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "collections.html", context)

def productview(request, id):
    context = None
    product =  Product.objects.filter(id = id).first()
    context = {'products': product}
    return render(request, "views.html", context)


def collectionsview(request, id):
    products =  Product.objects.filter(category = id, status = 0)
    context = {'products': products}
    return render(request, "index.html", context)