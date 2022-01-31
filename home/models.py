from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=False)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    phoneno = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='static/img/profile')
    state = models.CharField(max_length=100,null=True)


    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    cat = models.CharField(max_length=200)
    subcat = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img/project/')

    def __str__(self) -> str:
        return f"{self.tname} \t {self.pid}"

PROSSED = "pd"

STATUS_CHOICES = (
    ("PROSSED", "process"),
    ("SHIPING", "shiping"),
    ('ONTHEWAY', "ontheway"),
    ('PROSSED', "receved"),
)


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9,choices=STATUS_CHOICES,default=False)
    trasection_id = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self) -> str:
        return str(self.id)

    @property
    def get_cart_totle(self):
        orderitems = self.orderitem_set.all()
        totle = sum([item.get_totle for item in orderitems])
        return totle

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        totle = sum([item.quantity for item in orderitems])
        return totle

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_totle(self):
        totle = self.product.price * self.quantity
        return totle

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.address}"

# wishlist
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class WishlistItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    wishlists = models.ForeignKey(Wishlist,on_delete=models.SET_NULL,null=True)
