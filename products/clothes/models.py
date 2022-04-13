from django.db import models
from store.models import Product, Category

# Create your models here.

COLOR_CHOICES = (("Black", "Black"),
                 ("Brown", "Brown"),
                 ("Red", "Red"),
                 ("Gray", "Gray"),
                 ("Blue", "Blue"),
                 ("White", "White"),
                 ("Pink", "Pink")
                 )

SiZE_CHOICES = (("S", "S"),
                ("M", "M"),
                ("L", "L"),
                ("XL", "XL"),
                ("XXL", "XXL"),
                )


class Color(models.Model):
    name = models.CharField(max_length=200, null=True, choices=COLOR_CHOICES, default="Black")

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=200, null=True, choices=SiZE_CHOICES, default="S")

    def __str__(self):
        return self.name


class Clothes(Product):
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cat = Category.objects.get(cat_name='Clothes')
        self.category = cat

    def __str__(self):
        return self.product_name
