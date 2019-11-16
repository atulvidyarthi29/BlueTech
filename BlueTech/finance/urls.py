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
    path('expenditure/', views.expenditure, name="expenditure"),
    path('assets/', views.assets, name="assets"),
    path('liabilities/', views.liabilities, name="liabilities"),
    path('assets/current-assets/', views.current_assets, name="current_assets"),
    path('assets/intangible-assets/', views.intangible_assets, name="intangible_assets"),
    path('assets/investments/', views.investments, name="investments"),
    path('assets/payables/', views.payables, name="payables"),
    path('recivables/', views.recivables, name="recivables"),
    path('liabilities/current-liabilities/', views.current_liabilities, name="current_liabilities"),
    path('liabilities/longterm-liabilities/', views.longterm_liabilities, name="longterm_liabilities"),
    path('liabilities/stockholders-equity/', views.stockholders_equity, name="stockholders_equity"),
    path('transactions/ten-days/', views.ten_days_transactions, name="ten_days_transactions"),
    path('transactions/thirty-days/', views.thirty_days_transactions, name="thirty_days_transactions"),
    path('transactions/four-months/', views.four_months_transactions, name="four_months_transactions"),
    path('transactions/six-months/', views.six_months_transactions, name="six_months_transactions"),
    path('transactions/one-year/', views.one_year_transactions, name="one_year_transactions"),
]
