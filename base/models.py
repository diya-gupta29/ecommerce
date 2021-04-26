from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from authentication.models import Customer

# Create your models here.


Category_Choices = (
    ('Cakes', 'Cakes'),
    ('Bouquets', 'Gifts'),
    ('Chocolates','Chocolates'),
    ('Plants','Plants'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField(null = True)
    category = models.CharField(choices = Category_Choices,max_length = 100,null = True)
    item_image = models.ImageField(upload_to = 'item_img',null = True)

    def __str__(self):
        return str(self.id)

status_choices = (
    ('Delivered','Delivered'),
    ('Pending','Pending'),
    ('Cancelled','Cancelled'),
    ('Accepted','Accepted'),
    # ('On the way','On the way')
    ('Packed','Packed'),
    ('Dispatched','Dispatched')
)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity*self.item.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    def __str__(self):
        return str(self.id)

class OrderStatus(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices = status_choices,max_length = 15, default = 'Pending')

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity*self.item.discounted_price