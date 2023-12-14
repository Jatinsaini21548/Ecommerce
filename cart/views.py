from django.shortcuts import render
from store.views import *
from store.models import *
from django.http import JsonResponse




def addtocart(request):
    cart = Cart.objects.filter(user = request.user)
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            prod_qty = request.POST.get('quantity')
            if Cart.objects.filter(product = prod_id):
                messages.error(request, "Product already in cart")
            else:
                Cart.objects.create(user = request.user, product_id = prod_id, product_qty = prod_qty)              
    return render (request, 'cart.html', {'cart':cart})


def viewcart(request):
    cart = Cart.objects.filter(user = request.user)
    context = {'cart':cart}
    return render(request, "cart.html", context)

# def updatecart(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             if(Cart.objects.filter(user = request.user, product_id = prod_id)):
#                 prod_qty = int(request.POST.get('product_qty'))
#                 cart = Cart.objects.get(product_id = prod_id, user = request.user)
#                 cart.product_qty = prod_qty
#                 cart.save()
#     return redirect('/')


def update_cart(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            quantity = request.POST.get('quantity')
            prod_id = request.POST.get('product_cart_id')
            print("----------------------------", prod_id)
            cart = Cart.objects.get(id = prod_id)
            cart.product_qty = quantity
            cart.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def deletecartitem(request, id):
    user = request.user
    user_id = user.id
    cart_item = Cart.objects.filter(user=user_id, id=id)
    cart_item.delete()
    messages.success(request, "Product removed")
    return redirect('cart')



    




