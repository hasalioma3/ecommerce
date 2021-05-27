from django.contrib import admin
from . import models
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    search_fields=('user', 'name', 'email', )
    list_display=('user', 'name', 'email', )
class ProductAdmin(admin.ModelAdmin):
    search_fields=('name', 'price', 'digital', 'image', )
    list_display=('name', 'price', 'digital', 'image', )
class OrderAdmin(admin.ModelAdmin):
    search_fields=('customer__user__username', 'date_ordered', 'complete', )
    list_display=('customer', 'date_ordered', 'complete', 'transction_id', )
class OrderItemAdmin(admin.ModelAdmin):
    search_fields=('product', 'order', 'quantity', 'date_added', )
    list_display=('product', 'order', 'quantity', 'date_added', )
class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields=('customer__user__username', 'order__transction_id', )
    list_display=('customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_add', )

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem,OrderItemAdmin)
admin.site.register(models.ShippingAddress, ShippingAddressAdmin)
