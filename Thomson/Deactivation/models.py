from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    number = models.IntegerField()
    img = models.CharField(max_length=2000, default='https://pickaface.net/assets/images/slides/slide1.png')

    def __str__(self):
        return self.customer_name + "-" + self.mail + "-" + str(self.number)


class Order(models.Model):
    order_id = models.IntegerField()
    order_name = models.CharField(max_length=50)
    order_quantity = models.IntegerField()
    order_image = models.CharField(max_length=2000,
                                   default='https://www.iconexperience.com/_img/g_collection_png/standard/512x512/purchase_order.png')


    def __str__(self):
        return self.order_name + "-" + str(self.order_id) + "-" + str(self.order_quantity)
