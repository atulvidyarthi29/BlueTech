from django.forms import ModelForm
from django import forms
from Sales.models import Product, Customer, Purchase, Lead, ProductBought, Invoice

customer_type = (
    ('Vendor','Vendor'),
    ('Regular','Regular'),
    ('VIP','VIP'),
)

sex = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

status = (
    ("Active","Active"),
    ("Inactive","Inactive"),
)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CustomerForm(ModelForm):
    status = forms.ChoiceField(choices=status,widget=forms.RadioSelect)
    address = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model= Customer
        fields = "__all__"

class LeadForm(ModelForm):
    address = forms.CharField(widget=forms.Textarea, required=False)
    remarks = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model=Lead
        fields="__all__"


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ('purchased_from','date')

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_no', 'customer', 'date')


class ProductBoughtForm(ModelForm):
    class Meta:
        model = ProductBought
        fields = "__all__"
