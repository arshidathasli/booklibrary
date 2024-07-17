from django.urls import path
from .import views

urlpatterns=[

path("create-book", views.creatBook, name='create'),
    path('', views.listBook, name='listview'),
    path('detailsview/<int:book_id>/', views.detailsview, name='details'),
    path('updateview/<int:book_id>/', views.updateBook, name='update'),
    path('deleteview/<int:book_id>/', views.deleteview, name='delete'),
    path('author/', views.create_author, name='author'),
    path('search/',views.Search_book,name='search'),

    
    
]