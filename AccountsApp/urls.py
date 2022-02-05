from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),

    path('create_order/<str:pk>/',views.createOrder,name="create_order"),
    path('Update_order/<str:pk>/',views.UpdateOrder,name="update_order"),
    path('deleteOrder/<str:pk>/',views.deleteOrder,name="delete_order"),

]