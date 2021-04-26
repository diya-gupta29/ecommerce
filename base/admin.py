from django.contrib import admin
from .models import Item, Cart, Wishlist, OrderStatus

# Register your models here.
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(OrderStatus)
