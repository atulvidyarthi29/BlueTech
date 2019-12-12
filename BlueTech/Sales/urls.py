from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path('item/', views.add_item, name='add_item'),
    path('addcustomer/', views.add_customer, name="add_customer"),
    path('customerlist/', views.customer_list, name='customer_list'),
    # path('generatepdf/', views.GeneratePdf.as_view(), name="generate_pdf"),
    path('remove_customer/<int:pk>', views.remove_customer, name="remove_customer"),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
    path('customer_detail/<int:pk>', views.customer_detail, name='customer_detail'),
    path('remove_product/<str:pk>', views.remove_product, name="remove_product"),
    path('update_product/<str:pk>', views.update_product, name='update_product'),
    path('detail_product/<str:pk>', views.detail_product, name='detail_product'),
    # path('purchase_item',views.purchase_item, name='purchase_item'),
    path('sales_dashboard', views.sales_dashboard, name='sales_dashboard'),
    path('lead', views.lead_list, name='lead_list'),
    path('addlead/', views.add_lead, name="add_lead"),
    path('remove_lead/<int:pk>', views.remove_lead, name="remove_lead"),
    path('update_lead/<int:pk>', views.update_lead, name='update_lead'),
    path('restcustomer/', views.CustomerList.as_view(), name="restcustomer"),
    path('restproduct/', views.ProductList.as_view(), name="restproduct"),
    path('restlead/', views.LeadList.as_view(), name="restlead"),
    path('prodauto/', views.autocompleteModel, name='prodauto'),
    path('addinvoiceproduct/', views.add_invoice_product, name='add_invoice_product'),
    path('addinvoice', views.add_invoice, name="add_invoice"),
    path('invoicelist/', views.invoice_list, name='invoice_list'),
    path('show_invoice/<int:invoice_no>/', views.show_invoice, name='show_invoice'),
    path('weekgraph/',views.WeekGraph.as_view(),name='weekgraph'),
    path('yeargraph/',views.YearGraph.as_view(),name='yeargraph'),
    path('profileuser/',views.ProfileUser.as_view(),name='profileuser'),
]
