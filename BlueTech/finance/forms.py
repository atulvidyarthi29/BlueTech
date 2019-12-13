from django.forms import ModelForm
from .models import *


class SalesForm(ModelForm):
    class Meta:
        model = SalesAccount
        fields = '__all__'


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class PayableAccountForm(ModelForm):
    class Meta:
        model = PayableAccount
        fields = '__all__'


class LiabilityForm(ModelForm):
    class Meta:
        model = Liability
        fields = '__all__'
