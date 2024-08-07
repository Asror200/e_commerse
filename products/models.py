from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(BaseModel):
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

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return False

    def __str__(self):
        return self.name


class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    comment = models.TextField(null=True, blank=True)
    is_provide = models.BooleanField(default=True)  # so that we don't show commentaries when we want

    def __str__(self):
        return f'{self.name} , {self.comment} , {self.created_at} , {self.updated_at}'


class Order(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders', null=True)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.username} , {self.product}'
