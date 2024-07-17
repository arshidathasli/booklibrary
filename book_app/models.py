from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='book_media/')
    quantity=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.title)
