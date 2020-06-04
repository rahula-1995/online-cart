
from django.contrib import admin

# Register your models here.
from .models import product, Contact,Orders,category,OrderUpdate



class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id','name','email')
    list_display_links = ('order_id','name','email')
    search_fields = ('order_id','name','email')

admin.site.site_header ="corona warrior"
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(category)
admin.site.register(OrderUpdate)