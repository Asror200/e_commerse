from django.contrib import admin
from django.utils.html import format_html
from products.models import Product, Category, Comment, Order


# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'product_count')
    search_fields = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('products',)

    def product_count(self, obj):
        return obj.products.count()


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'get_image', 'is_product_count_more_than_zero', 'category')
    search_fields = ('name',)
    list_filter = ['category']

    def is_product_count_more_than_zero(self, obj):
        return obj.quantity > 0

    is_product_count_more_than_zero.boolean = True

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return None

    get_image.short_description = 'Image'


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'comment', 'product')
    list_filter = ('product',)

    def get_name(self, obj):
        return obj.name

    get_name.short_description = 'Username'


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('product',)
    list_filter = ['product']



