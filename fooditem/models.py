from django.db import models
from restaurant.models import Menu
# Create your models here.
class FoodItem(models.Model):
    food_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=7,decimal_places=2)
    menu_id = models.ForeignKey(Menu,on_delete=models.CASCADE)
    picture = models.ImageField(null=True,blank=True,upload_to="food_image")
    rating = models.DecimalField(null=True,blank=True,max_digits=2,decimal_places=2)
    item_category = models.CharField(max_length=255)
    def __str__(self):
        """Return string representation of our user"""
        return self.name