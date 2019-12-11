from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(PayableAccount)
admin.site.register(SalesAccount)
admin.site.register(Asset)
admin.site.register(Liability)


