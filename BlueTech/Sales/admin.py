from django.contrib import admin
from Sales.models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(ProductBought)
admin.site.register(Sale)
admin.site.register(SalesDesc)
admin.site.register(Lead)
admin.site.register(Purchase)