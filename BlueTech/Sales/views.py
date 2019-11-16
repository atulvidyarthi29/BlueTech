import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from Sales.forms import ProductForm, CustomerForm, PurchaseForm, LeadForm
# from Sales.utils import render_to_pdf
from .models import Product, Customer, Lead
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def add_item(request):
    products = Product.objects.all()
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        # print(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect("sales:add_item")
        return HttpResponse("Error")
    else:
        product_form = ProductForm()
    return render(request, 'Sales/items.html', {"product_form": product_form, "products": products})


def remove_product(request, pk):
    product = Product.objects.get(itemcode=pk)
    product.delete()
    return redirect("sales:add_item")


def update_product(request, pk):
    product = get_object_or_404(Product, itemcode=pk)
    product_form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            return redirect("sales:add_item")
        else:
            print(product_form.errors)
    return render(request, 'Sales/update_product.html', {"product": product_form})


def detail_product(request, pk):
    product = Product.objects.get(itemcode=pk)
    product_form = ProductForm(request.POST or None, instance=product)
    return render(request, 'Sales/product_detail.html', {"product": product_form, "products": product})


def add_customer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        CustomerForm.doj = datetime.date.today()
        if customer_form.is_valid():
            customer_form.save()
            return redirect("sales:customer_list")
        else:
            print(customer_form.errors)
            # return HttpResponse("Error")
    else:
        customer_form = CustomerForm()
    return render(request, "Sales/addcustomer.html", {"customer_form": customer_form})


def update_customer(request, pk):
    customers = Customer.objects.all()
    customer = get_object_or_404(Customer, id=pk)
    # customer = Customer.objects.get(id=pk)
    customer_form = CustomerForm(request.POST or None, instance=customer)
    if request.method == 'POST':
        if customer_form.is_valid():
            customer_form.save()
            return redirect("sales:customer_list")
        else:
            print(customer_form.errors)
    return render(request, 'Sales/update_customer.html', {"customer": customer_form})


def customer_list(request):
    customers = Customer.objects.all()

    return render(request, "Sales/clist.html", {"customers": customers})


def remove_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect("sales:customer_list")


# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         customers = Customer.objects.all()
#         pdf = render_to_pdf('Sales/clist.html', {"customers":customers})
#         return HttpResponse(pdf, content_type='application/pdf')

def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    customer_form = CustomerForm(request.POST or None, instance=customer)
    return render(request, 'Sales/customer_detail.html', {"customer_form": customer_form, "customer": customer})


# def purchase_item(request):
#     if request.method=='POST':
#         purchase_form=PurchaseForm(request.POST)
#         if purchase_form.is_valid():
#             purchase_form.save()
#             purchase_form = PurchaseForm()
#             return render(request,'sales/purchase_product.html',{'purchase_form':purchase_form})
#     purchase_form = PurchaseForm()
#     return render(request,'sales/purchase_product.html',{'purchase_form':purchase_form})

def sales_dashboard(request):
    department = request.user.employee.dept
    customer_val = Customer.objects.count()
    product_val = Product.objects.count()
    lead_val = Lead.objects.count()
    return render(request, 'Sales/sales_dashboard.html',
                  {'department': department, 'customer_val': customer_val, 'product_val': product_val,
                   'lead_val': lead_val})


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "Sales/Llist.html", {"leads": leads})


def add_lead(request):
    if request.method == "POST":
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead_form.save()
            return redirect("sales:lead_list")
        else:
            print(lead_form.errors)
            # return HttpResponse("Error")
    else:
        lead_form = LeadForm()
    return render(request, "Sales/addlead.html", {"lead_form": lead_form})


def update_lead(request, pk):
    leads = Lead.objects.all()
    lead = get_object_or_404(Lead, id=pk)
    # customer = Customer.objects.get(id=pk)
    lead_form = LeadForm(request.POST or None, instance=lead)
    if request.method == 'POST':
        if lead_form.is_valid():
            lead_form.save()
            return redirect("sales:lead_list")
        else:
            print(lead_form.errors)
    return render(request, 'Sales/update_lead.html', {"lead_form": lead_form})


def remove_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("sales:lead_list")


class CustomerList(APIView):

    def get(self, request):
        candidate = Customer.objects.all()
        serializer = CustomerSerializer(candidate, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)


class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)


class LeadList(APIView):

    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
