from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=500, null=True, blank=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='customer')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

    @property
    def photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
