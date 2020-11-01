from django.contrib import admin

from .models import *
class OrderAdmin(admin.ModelAdmin):
    list_display = [
    'customer','date_ordered','complete',

]

    class Meta:
        model = Order



admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
