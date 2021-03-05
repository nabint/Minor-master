from django.db import models
from django.db.models.signals import pre_save, post_save

class RestaurantManager(models.Manager):
    def create_restaurant(self,restaurant_name,address):
        restaurant = self.model(restaurant_name=restaurant_name,address=address)
        print(restaurant)
        restaurant.save(using=self.db)
        return restaurant



# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key = True)
    restaurant_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    picture = models.ImageField(null=True,blank=True,upload_to="restaurant_picture")
    objects = RestaurantManager()
    def __str__(self):
        """Return string representation of our user"""
        return str(self.restaurant_id)

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True,)
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE)
    def __str__(self):
        """Return string representation of our user"""
        return 'Menu of ' + self.restaurant.restaurant_name+ str(self.menu_id)

class Table(models.Model):
    table_id = models.AutoField(primary_key=True,)
    table_no = models.IntegerField(null=False)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    def __str__(self):
        """Return string representation of our user"""
        return self.restaurant.restaurant_name + ' - Table :' + str(self.table_id)

        
def generateMenu(sender,instance,created,*args,**kwargs):
    if created:
        menu = Menu(restaurant=instance)
        print(menu)
        print('creting Menu')
        menu.save()
post_save.connect(generateMenu,sender=Restaurant)
