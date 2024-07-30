from django.contrib import admin

from products.models import Product, Category, ProductComment

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductComment)