from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='products_thumbs/')
    image = models.ImageField(upload_to='products_images/')
    create_date = models.DateField()
    stock = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.category.name + ' > ' + self.product.name
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    phone = models.CharField(max_length=64)
 
    def __str__(self):
        return self.user.username + " Telefono: " + self.phone
    
    #funcion que siempre retorna una orden (se cambio nuevo_costumer por self ya que es un objeto y con esto traemos su escencia o self)
    def get_current_order(self):
        #verifica si ell cliente self tiene una orden 
        nueva_order = Order.objects.filter(customer = self).first()
        #si no es none lo retorna
        if nueva_order is None:
            #si nueva_order is none la creamos
            nueva_order = Order()
            nueva_order.customer = self
            nueva_order.shipping_address = self.shipping_address
            nueva_order.status = "PENDIENTE"
            #retornamos nueva_order
            nueva_order.save()

        return nueva_order
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    shipping_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32) # PENDIENTE #PAGADO

    def __str__(self):
        return self.customer.user.username + " Estado Orden: " + self.status


class OrderDetail(models.Model):
    # ORDER tiene muchos ORDER DETAIL
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # PRODUCT TIENE MUCHOAS ORDER  DETAIL
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=6) #9999.12
    quantity = models.DecimalField(decimal_places=2, max_digits=6) #9999.12

    def __str__(self):
        return str(self.order.id) + " " + self.product.name