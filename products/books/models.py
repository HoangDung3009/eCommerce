from django.db import models
from store.models import Product, Category


# Create your models here.
# Author
class Author(models.Model):
    author_name = models.CharField(max_length=500, blank=True, null=True)
    author_email = models.CharField(max_length=500, blank=True, null=True)
    author_phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.author_name


# Publisher
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=500, blank=True, null=True)
    publisher_email = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.publisher_name


# Book
class Book(Product):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cat = Category.objects.get(cat_name='Book')
        self.category = cat

    def __str__(self):
        return self.product_name
