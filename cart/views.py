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


def update_cart(request):
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


def checkout(request):
    user = request.user
    id = user.id
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('checkoutemail')
        address = request.POST.get('address')
        address_2 = request.POST.get('address2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        data = Register_user.objects.get( id =  id)
        data.first_name= first_name,
        data.last_name = last_name,
        data.address = address ,
        data.optional_address = address_2 ,
        data.country = country,
        data.state = state,
        data.zip = zip 
        data.save()
        return redirect ('payment')
    return render(request, 'checkout.html')


def payment(request):
    user_id = request.user.id
    cart_items = Cart.objects.filter(user=user_id)

    for cart_item in cart_items:
        cart_item.total_price = cart_item.product.selling_price * cart_item.product_qty

    total_price = sum(cart_item.total_price for cart_item in cart_items)

    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'payment.html', context)


def address_select(request):
    user = request.user
    user_id = user.id
    bill_detail = Register_user.objects.filter(id = user_id)
    context =  {'billdetail': bill_detail}
    return render(request, 'address_select.html', context)





