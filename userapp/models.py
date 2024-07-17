from django.db import models
from accounts.models import UserProfile 
from book_app.models import Book
# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)  
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)  

    def __str__(self):
        return f'{self.book.title} - {self.quantity}'
    
class Orders(models.Model):
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    mode = models.CharField(max_length=20, default='COD')

    def __str__(self):
        return f'{self.user.user.username} - {self.amount}'
    
class OrderItems(models.Model) :
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)  
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)  

    def __str__(self):
        return f'{self.book.title} - {self.quantity}'
    