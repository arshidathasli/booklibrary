from django.urls import path
from . import views

urlpatterns = [   


    path('index/',views.index),
    path('register/',views.register_user,name='register'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logOut,name='logout'),

]