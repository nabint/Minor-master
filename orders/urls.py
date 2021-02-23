from django.urls import path, include
from orders import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    path('o/',views.OrderView.as_view()),
    path('o/<int:pk>/',views.OrderView.as_view()),
    path('oi/',csrf_exempt(views.OrderItemView.as_view())),
    path('oi/<int:pk>/',views.OrderItemView.as_view()),
    path('currentorders/',views.order_view)
]