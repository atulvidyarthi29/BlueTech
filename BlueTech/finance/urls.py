from django.urls import path
from . import views

app_name = "finance"   


urlpatterns = [
    path('', views.finance_home, name="finance_home"),
    path('tracking/', views.finance_tracking, name="finance_tracking"),
    path('reports/', views.finance_reports, name="finance_reports"),
    path('management/', views.finance_management, name="finance_management"),
    path('projection/', views.finance_projection, name="finance_projection"),
    path('transactions/', views.transactions, name="transactions"),
    path('income/', views.income, name="income"),
    path('asset-income/', views.income_asset, name="asset_income"),
    path('expenditure/', views.expenditure, name="expenditure"),
    path('liabilities/', views.liabilities, name="liability_expenditure"),
]
