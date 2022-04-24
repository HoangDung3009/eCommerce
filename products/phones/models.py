from django.db import models
from store.models import Product, Category


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Phone(Product):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cat = Category.objects.get(cat_name='Phone')
        self.category = cat

    def __str__(self):
        return self.product_name

    @property
    def photo_url(self):
        if self.product_thumb and hasattr(self.product_thumb, 'url'):
            return self.product_thumb.url
