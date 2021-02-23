from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from fooditem import serializers
from fooditem.models import FoodItem
import requests
from restaurant.models import Menu, Restaurant
from restaurant import serializers as res_serializers
# Create your views here.
class FoodItemView(APIView):
    serializers_class = serializers.FoodItemSerializers

    def get(self,request,format = None):
        
        qs = FoodItem.objects.filter(menu_id=request.data['menu_id'])
        # menu_qs = Menu.objects.filter(menu_id=)
        res_qs = Restaurant.objects.filter()
        # qs = FoodItem.objects.all()
        res_serializer = res_serializers.RestaurantSerializer(qs[0].menu_id.restaurant)
        print(res_serializer.data)
        serializer = serializers.FoodItemSerializers(qs,many=True)
        food_item = {'food':serializer.data,'restaurant':res_serializer.data}
        return Response(food_item)

    def post(self,request):
        serializer = self.serializers_class(data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            name = serializer.validated_data.get('name')
            return Response({'Item has been added':name})
        else:
            return Response(serializer.error_messages)
    
    def delete(self,request,pk):
        food_item = get_object_or_404(FoodItem.objects.all(),pk=pk)
        food_item.delete()
        return Response({"message": "FoodItem with id `{}` has been deleted.".format(pk)},status=204)

def menu_view(request):
    restaurant = Restaurant.objects.filter(restaurant_name=request.user.name)
    menu = Menu.objects.filter(restaurant = restaurant[0].restaurant_id)
    food_item = FoodItem.objects.filter(menu_id=menu[0])
    fitems = {
        "food_items":food_item
    }
    print(food_item)
    for item in food_item:
        print(item.name)
    
    template="MenuPage.html"
    return render(request,template,fitems)