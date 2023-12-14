from django.shortcuts import render
from store.views import *
from store.models import *


def addtocart(request):
     
    if request.method == 'POST':
        print("--------------------------------------. I am here ")
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            product_check = Product.objects.get(id = prod_id)
            prod_qty = request.POST.get('quantity')
            Cart.objects.create(user = request.user, product_id = prod_id, product_qty = prod_qty)
            # if(product_check):
            #     if(Cart.objects.filter(user = request.user.id, product_id = prod_id)):
            #          messages.error(request, "product already")
            #     else:
            #         prod_qty = request.POST.get('quantity')

            #         if product_check.quantity >= prod_qty:
            #             Cart.objects.create(user = request.user, product_id = prod_id, product_qty = prod_qty)
            #             return JsonResponse({'status', "Product added succesfully"}) 
            #         else:
            #             return JsonResponse({'status', "Only" + str(product_check.quantity)+ " quantity available"}) 
                 
            # else:
            #     return JsonResponse({'status', "No such product found"})    
        
             
    return render (request, 'cart.html')


def viewcart(request):
    cart = Cart.objects.filter(user = request.user)
    context = {'cart':cart}
    return render(request, "cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user = request.user, product_id = prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id = prod_id, user = request.user)
            cart.product_qty = prod_qty
            cart.save()
    return redirect('/')


def deletecartitem(request):
    if request.method == 'POST':
       prod_id = int(request.POST.get('product_id'))
       if(Cart.objects.filter(user = request.user, product_id = prod_id)):
           cartitem = Cart.objects.get(product_id =  prod_id, user = request.user)
           cartitem.delete()
           cartitem.save()
    return redirect('/')



    




