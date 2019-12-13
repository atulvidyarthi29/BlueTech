from collections import defaultdict
from datetime import date, timedelta
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.utils import json

from Sales.forms import ProductForm, CustomerForm, PurchaseForm, LeadForm, InvoiceForm, ProductBoughtForm
# from Sales.utils import render_to_pdf
from .models import Product, Customer, Lead, Invoice
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
import  json
import requests

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
            pass
            # print(product_form.errors)
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
            pass
            # print(customer_form.errors)
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
            pass
            # print(customer_form.errors)

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
    cv = week_chart()
    yc = yearly_chart()
    yc0 = json.dumps(yc[0])
    yc1 = json.dumps(yc[1])
    cv1 = json.dumps(cv[1])
    cv0 = json.dumps(cv[0])
    return render(request, 'Sales/sales_dashboard.html',
                  {'department': department, 'customer_val': customer_val, 'product_val': product_val,
                   'lead_val': lead_val, 'cv0': cv0, 'cv1': cv1, 'yc0': yc0, 'yc1': yc1})


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
            pass
            # print(lead_form.errors)
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
            pass
            # print(lead_form.errors)
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


def add_invoice_product(request):
    invoice_no = request.session['invoice_no']
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    products = invoice.productbought_set.all()
    if request.method == "POST":
        product_bought_form = ProductBoughtForm(request.POST)
        product = request.POST.get("search")
        product = Product.objects.get(itemname=product)
        price = product.price
        quantity = request.POST.get("quantity")
        amount = int(price) * int(quantity)
        product_bought_form.invoice = invoice
        product_bought_form.amount = amount
        pb = ProductBought()
        pb.product = product
        pb.amount = amount
        pb.quantity = quantity
        pb.invoice = invoice
        invoice.total_amount = invoice.total_amount + amount
        invoice.save()
        pb.save()
        return redirect("sales:add_invoice_product")
        # if product_bought_form.is_valid():
        #     product_bought_form.save()
        #     redirect("sales:add_invoice_product", invoice_no=invoice_no)
        # else:
        #     return HttpResponse("Form is not valid." + str(request.session['invoice_no']))
    else:
        context = {
            "product_bought_form": ProductBoughtForm(),
            "products": products,
            "name": invoice.customer.company_name,
            "date": invoice.date,
            "invoice": invoice
        }
        return render(request, "Sales/add_invoice_product.html", context)


def add_invoice(request):
    if request.method == "POST":
        invoice_form = InvoiceForm(request.POST)
        if invoice_form.is_valid():
            inv = invoice_form.save()
            # return HttpResponse("Invoice Added")
            request.session["invoice_no"] = inv.invoice_no
            return redirect("sales:add_invoice_product")
        else:
            return HttpResponse("Error")
    else:
        invoice_form = InvoiceForm()
        return render(request, "Sales/add_invoice.html", {"invoice_form": invoice_form})


def autocompleteModel(request):
    search_qs = Product.objects.filter(itemname__startswith=request.GET['search'])
    # print(request.GET['search'])
    results = []
    for r in search_qs:
        results.append(r.itemname)
    # print(results)
    resp = request.GET['callback'] + '(' + json.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')


def invoice_list(request):
    invoices = Invoice.objects.all()
    invoices.reverse()
    return render(request, 'sales/invoice_list.html', {'invoices': invoices})


def show_invoice(request, invoice_no):
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    products = invoice.productbought_set.all()
    context = {
        "invoice": invoice,
        "products": products,
    }
    # print(context)
    return render(request, 'sales/show_invoice.html', context)


def week_chart():
    N = 7
    current_date = date.today().isoformat()

    chart_values = defaultdict(float)
    for i in range(N):
        days_before = (date.today() - timedelta(days=i)).isoformat()
        for j in Invoice.objects.filter(date=days_before):
            chart_values[days_before] += j.total_amount
    cv = []
    cv.append(list(chart_values.keys()))
    cv.append(list(chart_values.values()))
    return cv


def yearly_chart():
    chart_values = defaultdict(float)
    for i in range(12):
        for j in Invoice.objects.filter(date__month=i + 1):
            chart_values[j.date.month] += j.total_amount

    ycvx = list(chart_values.keys())
    ycvy = list(chart_values.values())
    ycvxy = [ycvx, ycvy]
    # ycvx = json.dumps(ycvx)
    # ycvy = json.dumps(ycvy)
    # ycvxy = [ycvx, ycvy]
    return ycvxy



# week_chart()

class WeekGraph(APIView):

    def get(self, request):
        leads = week_chart()
        return JsonResponse(leads, safe=False)

class YearGraph(APIView):
    def get(self, request):
        leads = yearly_chart()
        return JsonResponse(leads, safe=False)

# class get_email_pass(generics.ListCreateAPIView):
#     queryset = userlogin.objects.all()
#     serializer_class = user_login


# class User_api(APIView):
# def user_login(request):
#
#     username="sana"
#     password="san"
#     data = {
#         'username': username,
#         'password': password,
#
#     }
#     # print(data)
#     data = json.dumps(data)
#     headers = {
#         "Content-Type": "application/json",
#         "accept": "application/json",
#         # 'Authorization': 'JWT ',
#         #   Authorization: `JWT ${localStorage.getItem('token')}`,
#     }
#
#     API_ENDPOINT = 'http://127.0.0.1:8000/token-auth/'
#     r = requests.post(url=API_ENDPOINT, data=data, headers=headers)
#     pastebin_url = r.content
#     print("The pastebin url is :%s" % pastebin_url)
#     k = r.json()
#     # print(k)
#     token_data = k["token"]
#     # print(token_data)
#
#     file = open('token.txt', 'w')
#     file.write(token_data)
#     file.close()
#
#     return HttpResponse('djsabhuhh')
#
#     file = open('token.txt', 'r')
#     tokendata= file.read()
#     file.close()

# def abcd(request):
#     print(tokendata)
#     headers = {
#         "Content-Type": "application/json",
#         "accept": "application/json",
#         'Authorization': 'JWT ' + tokendata,
#         #   Authorization: `JWT ${localStorage.getItem('token')}`,
#     }
#     username='deepesh'
#     email='deepesh.b17@iiits.in'
#     first_name='deepesh'
#     data={
#         'username':username,
#         'email':email,
#         'first_name':first_name,
#     }
#     data=json.dumps(data)
#     api_url=('')
# class saana(generics.ListCreateAPIView):
#     queryset = User.Objects.all()
#     serializer_class = userserializer

# class ProfileUser(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = userdataSerializer
#
#     def get_queryset(self):
#         username=self.request.user
#         print(username)
#         user_instance=User.objects.get(username=username)
#         #print(user_instance.email)
#         return Employee.objects.filter(user=user_instance)

class ProfileUser(APIView):
    queryset = Employee.objects.all()
    serializer_class = userdataSerializer
    def get(self,request):
        username=self.request.user
        user_instance=User.objects.get(username=username)
        #print(user_instance.email)
        list1=[]
        list1.append(user_instance.email)
        a=Employee.objects.filter(user=user_instance)
        for i in a:
            list1.append(i.first_name)
            list1.append(i.last_name)
            list1.append(i.position)
        #print(list1)

        return JsonResponse(list1,safe=False)

