from django.urls import path, include
from restaurant import views
urlpatterns=[
    path('',views.RestaurantView.as_view()),
    path('tables/',views.table_view)
]