"""
Build the admin for product upload.
"""

from django.contrib import admin
from .models import Product, Category


"""
Include the list_displays for the admin.
"""
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'size',
        'weight'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'pk'
    )

    ordering = ('pk',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

