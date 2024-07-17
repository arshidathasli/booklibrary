from django.urls import path
from .import views

urlpatterns=[
    path('', views.listBook, name='listviewuser'),
    path('detailsview/<int:book_id>/', views.detailsview, name='details'),
    path('search/',views.Search_book,name='Search_book'),
    path('addtocart/<int:book_id>/',views.add_to_cart,name='addtocart'),
    path('view_cart/',views.view_cart,name='viewcart'),
    path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>/',views.decrease_quantity,name="decrease_quantity"),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orders/', views.view_orders, name='orders'),
    path('order_cod/', views.place_order_cod, name='order_cod'),
    path('order_gateway/', views.view_orders, name='order_gateway'),




]
