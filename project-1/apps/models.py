from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django_resized import ResizedImageField


class BaseCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseCreatedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseCreatedModel):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    info = models.JSONField(default=dict)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.quantity > 0

    @property
    def is_new(self):
        return now() - timedelta(days=3) < self.created_at

    class Meta:
        ordering = ['-created_at']


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    # image = models.ImageField(upload_to='products/')
    image = ResizedImageField(size=[500, 600], crop=['middle', 'center'], upload_to='products/')

    def __str__(self):
        return self.product.name


class User(AbstractUser, BaseCreatedModel):
    intro = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)


