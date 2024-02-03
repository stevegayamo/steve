from django.contrib import admin
from .models import Appliance, ApplianceImage, Category, Cart, CartItem, Order, OrderItem

# Register your models here.
admin.site.register(Appliance)
admin.site.register(ApplianceImage)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

