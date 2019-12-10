from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import SalesForm, AssetForm, PayableAccountForm, LiabilityForm
from .models import SalesAccount, Asset, PayableAccount, Liability
from datetime import date


# Create your views here.

def finance_home(request):
    department = request.user.employee.dept
    return render(request, "finance/home.html",
                  context={'department': department, 'user': request.user.employee})


def income(request):
    if request.method == 'POST':
        sales_form = SalesForm(request.POST)
        if sales_form.is_valid():
            sales_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse("Some Error Occured")
    else:
        sales_form = SalesForm()
    data = SalesAccount.objects.all()
    # today = date.today()
    # net_week = PayableAccount.objects.filter(date_from__month__gte=today.day - 7,
    #                                          date_to__month__lte=today.day).aggregate(Sum('price'))
    # net_month = PayableAccount.objects.filter(date_from__month__gte=today.month - 1,
    #                                           date_to__month__lte=today.month).aggregate(Sum('price'))
    # net_year = PayableAccount.objects.filter(date_from__month__gte=today.year - 1,
    #                                          date_to__month__lte=today.year).aggregate(Sum('price'))
    # print(net_week,net_month,net_year)
    # # overall_net =  PayableAccount.objects.filter()
    return render(request, "finance/tracking/income.html",
                  context={'data': data, 'sales_form': sales_form})


def income_asset(request):
    if request.method == 'POST':
        asset_form = AssetForm(request.POST)
        if asset_form.is_valid():
            asset_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse("Some Error occurred")
    else:
        asset_form = AssetForm()
    data = Asset.objects.all()
    return render(request, "finance/tracking/asset_income.html",
                  context={'data': data, 'asset_form': asset_form})


def expenditure(request):
    if request.method == 'POST':
        payable_account_form = PayableAccountForm(request.POST)
        if payable_account_form.is_valid():
            payable_account_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse("Some Error Occured")
    else:
        payable_account_form = PayableAccountForm()
    data = PayableAccount.objects.all()
    return render(request, "finance/tracking/expenditure.html",
                  context={'data': data, 'payable_account_form': payable_account_form})


def liabilities(request):
    if request.method == 'POST':
        liability_form = LiabilityForm(request.POST)
        if liability_form.is_valid():
            liability_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse("Some Error occurred")
    else:
        liability_form = LiabilityForm()
    data = Liability.objects.all()
    return render(request, "finance/tracking/liabilities.html",
                  context={'data': data, 'liability_form': liability_form})


def finance_tracking(request):
    return render(request, "finance/tracking.html")


def finance_reports(request):
    return render(request, "finance/reports.html")


def finance_management(request):
    return render(request, "finance/management.html")


def finance_ratios(request):
    return render(request, "finance/ratio.html")


def finance_projection(request):
    return render(request, "finance/projections.html")


def transactions(request):
    return render(request, "finance/tracking/transactions.html")
