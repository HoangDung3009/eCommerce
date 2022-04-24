from django.db import models

#Category
class Category(models.Model):
    cat_name = models.CharField(max_length=500, blank=True, null=True)
    cat_description = models.TextField(max_length=500, blank=True, null=True)
    cat_thumb = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.cat_name

    @property
    def photo_url(self):
        if self.cat_thumb and hasattr(self.cat_thumb, 'url'):
            return self.cat_thumb.url


# Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=500, blank=True, null=True)
    price = models.FloatField(default=0.00, null=True)
    product_thumb = models.ImageField(upload_to='product/', null=True, blank=True)
    product_description = models.TextField(blank=True, null=True)
    unit_in_stock = models.IntegerField(null=True)
    isActive = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

    @property
    def photo_url(self):
        if self.product_thumb and hasattr(self.product_thumb, 'url'):
            return self.product_thumb.url
