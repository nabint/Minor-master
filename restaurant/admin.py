from django.contrib import admin
from restaurant.models import Restaurant,Menu,Table
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Table)