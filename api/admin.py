from django.contrib import admin
from .models import Product, ProductImage, CartItem, Order, Cart

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Cart)