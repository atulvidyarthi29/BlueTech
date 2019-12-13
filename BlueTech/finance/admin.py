from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(PayableAccount)
admin.site.register(SalesAccount)
admin.site.register(Asset)
admin.site.register(FundApplication)
admin.site.register(LiabilitySources)
admin.site.register(ShareholderFunds)
admin.site.register(FinancialYear)
admin.site.register(Profit)

