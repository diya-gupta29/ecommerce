from django.shortcuts import render, redirect
from django.views import View
from .models import Item,Cart, Wishlist, OrderStatus
from authentication.models import Customer
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homeView(request):
    return render(request,'base/home.html')

def cake(request):
    cakes = Item.objects.filter(category = 'Cakes')
    return render(request,'base/item_list.html',{'items':cakes})

def chocolates(request):
    chocolates = Item.objects.filter(category = 'Chocolates')
    return render(request,'base/item_list.html',{'items':chocolates})

def plants(request):
    plants = Item.objects.filter(category = 'Plants')
    return render(request,'base/item_list.html',{'items':plants})

def special(request):
    special = []
    for p in Item.objects.filter(category = 'Plants'):
        special.append(p)
    for c in Item.objects.filter(category='Cakes'):
        special.append(c)
    return render(request,'base/item_list.html',{'items':special})

def anniversary(request):
    special = []
    for p in Item.objects.filter(category = 'Bouquets'):
        special.append(p)
    for c in Item.objects.filter(category='Cakes'):
        special.append(c)
    return render(request,'base/item_list.html',{'items':special})

def birth(request):
    special = []
    for p in Item.objects.filter(category = 'Cakes'):
        special.append(p)
    for c in Item.objects.filter(category='Bouquets'):
        special.append(c)
    return render(request,'base/item_list.html',{'items':special})

def gifts(request):
    special = []
    for p in Item.objects.filter(category = 'Chocolates'):
        special.append(p)
    for c in Item.objects.filter(category='Bouquets'):
        special.append(c)
    for p in Item.objects.filter(category = 'Plants'):
        special.append(p)
    return render(request,'base/item_list.html',{'items':special})


def bouquets(request):
    bouquets = Item.objects.filter(category = 'Bouquets')
    return render(request,'base/item_list.html',{'items':bouquets})

def itemDetail(request,id):
    item = Item.objects.get(id = id)
    item_already_in_cart = False
    item_already_in_wishlist = False
    if request.user.is_authenticated:
      item_already_in_cart = Cart.objects.filter(Q(item = item.id) & Q(user=request.user)).exists()
      item_already_in_wishlist = Wishlist.objects.filter(Q(item = item.id) & Q(user=request.user)).exists()
    return render(request,'base/itemDetail.html',{'item':item,'item_already_in_cart':item_already_in_cart,'item_already_in_wishlist':item_already_in_wishlist})

def addToCart(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    user = request.user
    print(request.user)
    item_id = request.GET.get('item_id')
    print("#########################3")
    print(item_id)
    print("#########################")
    item_id = Item.objects.get(pk=item_id)
    if Cart.objects.filter(Q(item = item_id.id) & Q(user=request.user)).exists():
        pass
    else:
        Cart(user=user,item=item_id).save()
    # return render(request,'app/addtocart.html')
    return redirect('/cart_items')

def wishlist(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    user = request.user
    print(request.user)
    item_id = request.GET.get('item_id')
    print("#########################3")
    print(item_id)
    print("#########################")
    item_id = Item.objects.get(pk=item_id)
    Wishlist(user=user,item=item_id).save()
    # return render(request,'app/addtocart.html')
    return redirect('/wishlist_items')

def wishlist_items(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    user =request.user
    wishlist = Wishlist.objects.filter(user=user)
    if wishlist:
        return render(request,'base/addwishlist.html',{'items':wishlist})
    else:
        return render(request,'base/emptywishlist.html')


def cart_items(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    user =request.user
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    total_amount = 0.0
    cart_item = [p for p in Cart.objects.all() if p.user == user]
    if cart_item:
        for item in cart_item:
            amt = (item.quantity * item.item.discounted_price)
            amount+=amt
        total_amount = amount+shipping_amount

        return render(request,'base/addtocart.html',{'carts':cart,'amount':amount,'total_amount':total_amount})
    else:
        return render(request,'base/emptycart.html')

def increment(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id) & Q(user=request.user))
        # c = Cart.objects.get(item=item_id)
        print("##########33")
        print(c)
        print("#############")
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0
        cart_item = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_item:
            for item in cart_item:
                amt = (item.quantity * item.item.discounted_price)
                amount+=amt
            total_amount = amount+shipping_amount

        data = {
        'quantity':c.quantity,
        'amount':amount,
        'total_amount':total_amount,
        }
        return JsonResponse(data)


def decrement(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0
        cart_item = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_item:
            for item in cart_item:
                amt = (item.quantity * item.item.discounted_price)
                amount+=amt
            total_amount = amount+shipping_amount

        data = {
        'quantity':c.quantity,
        'amount':amount,
        'total_amount':total_amount,
        }
        return JsonResponse(data)

def remove_item(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Cart.objects.get(Q(item=item_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0
        cart_item = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_item:
            for item in cart_item:
                amt = (item.quantity * item.item.discounted_price)
                amount+=amt
            total_amount = amount+shipping_amount

        data = {
        'amount':amount,
        'total_amount':total_amount,
        
        }
        return JsonResponse(data)

def remove_wish(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        c = Wishlist.objects.get(Q(item=item_id) & Q(user=request.user))
        c.delete()
        data = {
        'amount':12
        
        }
        return JsonResponse(data)

@login_required
def checkout(request):
    user = request.user
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    total_amount = 0.0
    cart_item = [p for p in Cart.objects.all() if p.user==request.user]
    if cart_item:
        for item in cart_item:
            amt = (item.quantity * item.item.discounted_price)
            amount+=amt
        total_amount = amount+shipping_amount
    
    client = razorpay.Client(auth=('rzp_test_2Pu0VavB8Bm92Z', 'VCcEjHrnti5VhwiYQNlVJXFN'))
    if cart_item:
        payment = client.order.create({'amount': total_amount*100, 'currency': 'INR','payment_capture': '1'})
        return render(request,'base/checkout.html',{'address':address,'total_amount':total_amount,'cart_items':cart_items,'payment': payment})
    return render(request,'base/emptycart.html')

def payment_done(request):
    print("##################")
    custid = request.GET.get('custid')
    user = request.user
    cus = Customer.objects.get(id = custid)
    cart_items = Cart.objects.filter(user = user)
    for c in cart_items:
        OrderStatus(user = user,customer=cus, item = c.item,quantity = c.quantity).save()
        c.delete()
    return redirect("/review_orders")

def review_orders(request):
    orders_placed = OrderStatus.objects.filter(user = request.user)
    if orders_placed:
        return render(request,'base/orders.html',{'orders_placed':orders_placed})
    return render(request,'base/emptyorder.html')

def filter_view(request,flag=1,amount=1000,cat=1):
    #below
    if cat==1:
        category = 'Cakes'
    elif cat==2:
        category = 'Chocolates'
    elif cat==3:
        category = 'Plants'
    else:
        category = 'Bouquets'
    if flag==0:  
        items = Item.objects.filter(category='Cakes').filter(discounted_price__lt=float(amount)) 
    else:  
        items = Item.objects.filter(category='Cakes').filter(discounted_price__gt=float(amount)) 
    return render(request,'base/item_list.html',{'items':items})
        
