from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)
    discount = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def product_status(self):
        if self.quantity > 0:
            return True
        return False

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return False

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # to limit bad words
    @property
    def comment_check(self):
        # for bad words
        bad_words = ['love']
        if self.comment:
            for word in bad_words:
                if word not in self.comment:
                    return True
            return False

    def __str__(self):
        return self.comment


class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders', null=True)
    username = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
