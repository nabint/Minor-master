from django.db import models
from fooditem.models import FoodItem
from restaurant.models import Table
# Create your models here.


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.TimeField(auto_now_add=True)
    table_no = models.OneToOneField(Table, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of our user"""
        return self.table_no.restaurant.restaurant_name + ' - Table -' + str(self.table_no)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    fooditem = models.ForeignKey(
        FoodItem, verbose_name="FOOD", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    status_1 = 'Served'
    status_2 = 'Cooking'
    status_choices = [
        (status_1,'Order is Served'),
        (status_2,'Order is Cooking')
    ]

    status = models.CharField(
        max_length=30,
        default = status_2,
        choices = status_choices)


    

    def __str__(self):
        return str(self.fooditem)
