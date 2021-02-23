from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from orders import serializers,models
from fooditem.models import FoodItem
from fooditem.serializers import FoodItemSerializers
from restaurant.serializers import TableSerializer
import json
import requests
from orders.models import OrderItem,Order
from django.http import JsonResponse
from restaurant.models import Restaurant, Table

from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie





# Create your views here.
class OrderView(APIView):
    serializer_class = serializers.OrderSerializers
    orderitem_sc = serializers.OrderItemSerializers
    fooditem_sc = FoodItemSerializers
    def get(self,request):
        qs = Order.objects.filter(table_no=request.data['tableno'])
        obj = Order.objects.get(table_no=request.data['tableno'])
        print(obj.pk)
        serializers = self.serializer_class(qs,many=True)
        orderitem_qs = OrderItem.objects.filter(order_id = obj.pk)
        orderitem_s = self.orderitem_sc(orderitem_qs,many=True)
        orderitem_list = list(orderitem_s.data)
        foodlist = []
        for x in range(len(orderitem_list)):
            orderitem_dict = dict(orderitem_list[x])
            fooditem_qs = FoodItem.objects.filter(food_id=orderitem_dict['fooditem'][0])
            fooditem_s = self.fooditem_sc(fooditem_qs,many=True)
            foodlist.append(fooditem_s.data)

        order = {"Orders":serializers.data,"OrderItems":orderitem_s.data,"FooItem":foodlist}
        return JsonResponse(order)
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response('Saveed')
    def delete(self,request,pk):
        table_order = get_object_or_404(Order.objects.all(),pk=pk)
        table_order.delete()
        return Response({"message": "Order with table No `{}` has been deleted.".format(pk)},status=204)




class OrderItemView(APIView):
    serializer_class = serializers.OrderItemSerializers
    def post(self,request,pk=None,format=None):
        table_qs = Table.objects.filter(table_no = request.data['tableno'])
        table = list(table_qs)[0]
        # print(table)
        check_ob = Order.objects.filter(table_no=table).count()
        if(check_ob <=0 ):
            
            new_order = Order(table_no=table)
            new_order.save()
        
        order_qs = Order.objects.filter(table_no = table)
        order = list(order_qs)[0]
        print(order)
        food = FoodItem.objects.get(name=request.data['name'])
        print(food)
        orderi = OrderItem(order=order,fooditem=food,quantity=request.data['quantity'])
        
        orderi.save()
        
        
        return Response('Success')
    
    
    def delete(self, request, pk):
        # Get object with this pk
        order_item = get_object_or_404(OrderItem.objects.all(), pk=pk)
        order_item.delete()
        return Response({"message": "OrderItem with id `{}` has been deleted.".format(pk)},status=204)

def order_view(request):
    restaurant = Restaurant.objects.filter(restaurant_name=request.user.name)
    tables = Table.objects.filter(restaurant=restaurant[0])
    order_items = []
    for table in tables:
        order = Order.objects.filter(table_no=table)
        if order.exists():
            order_item = OrderItem.objects.filter(order=order[0].order_id)
            print(order_item)
            order_items.append((order_item))
    o_items ={
        'order_items':order_items[0]
    }

    template="OrdersPage.html"
    return render(request,template,o_items)
    
