from os import name, truncate
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):#staff table
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)#location
    email = models.CharField(max_length=200, null=True)#role

    def __str__(self):
        return self.name

class Product(models.Model):#assets
    #Make,Model,Category,name,barcode,serialNo.<Filter for the Logged in User>
    name = models.CharField(max_length=200, null=True)
    price =models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    #image
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url='' 
        return url
from django.utils import timezone

class Order(models.Model):#delivery note
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)#Staff
    date_ordered= models.DateTimeField(auto_now_add=True)#Date Dispatched
    complete = models.BooleanField(default=False)#dispatched?
    transction_id = models.CharField(max_length=200, null=True)#delivery note
    #from location #set to current user location
    #to location #select a location


    def __str__(self):
        return str(self.id)

    @property
    def key1(self):
        return str(self.id).zfill(6)

    @property
    def shipping(self):
        shipping =False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total = float(sum([item.get_total for item in orderitems]))
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):#Assettrans
    #Asset
    product =models.ForeignKey(Product,verbose_name="Item Name", on_delete=models.CASCADE, null=True, blank=True)
    #delivery note
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Order No")
    #if category:prompt: default 1
    quantity = models.IntegerField(default=0, null=True, blank=True)
    #date dispatched
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.product.name)
    @property
    def get_total(self):
        total =self.product.price *self.quantity
        return total

class ShippingAddress(models.Model):#i don't need.
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.address
    