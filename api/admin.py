from django.contrib import admin
from .models import Product, ProductImages,CartItem,Order

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(CartItem)
admin.site.register(Order)