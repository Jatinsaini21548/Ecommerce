from django.shortcuts import render
from store.views import *
from store.models import *

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    print("collection view")
    return render(request, "collections.html", context)

def productview(request, cate_slug, prod_slug):
    print("this is product view")
    context = None
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
            print('productview if')
        else:
            if request.method == 'POST':
               if request.user.is_authenticated:
                  print('product view else')
                  prod_id = int(request.POST.get('prod_id'))
                  product_check = Product.objects.get(id = prod_id)
                  prod_qty = request.POST.get('quantity')
                  Cart.objects.create(user = request.user, product_id = prod_id, product_qty = prod_qty)
    else:
        messages.error(request, "No such Category Found")
        return redirect('collections')
    return render(request, "views.html", context)



def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(slug=slug)
        category_name = Product.objects.filter(slug=slug).first()
        context = {'products': products, 'category_name': category_name}
        print("collections2 view")
        return render(request, "index.html", context)
    else:
        messages.warning(request, "No such category Found")
        return redirect('collections')