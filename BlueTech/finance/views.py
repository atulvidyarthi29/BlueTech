from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import SalesForm, AssetForm, PayableAccountForm, LiabilityForm
from .models import SalesAccount, Asset, PayableAccount, Liability, FundApplication,LiabilitySources,ShareholderFunds,FinancialYear,Profit
from datetime import date
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def finance_home(request):
    department = request.user.employee.dept
    return render(request, "finance/home.html",
                  context={'department': department, 'user': request.user.employee})


@login_required
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
    data_chart_date = SalesAccount.objects.values('date').order_by('date').annotate(pricee=Sum('price'))[:20]
    date = []
    net_amount = []
    for q in data_chart_date:
        date.append(q['date'].strftime('%Y-%m-%d'))
        net_amount.append(q['pricee'])

    print(date, net_amount)
    return render(request, "finance/tracking/income.html",
                  context={'data': data, 'sales_form': sales_form, 'date': date, 'net_amount': net_amount, })


@login_required
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
    data_chart_date = Asset.objects.values('date').order_by('date').annotate(pricee=Sum('tax_levied'))[:20]
    date = []
    net_amount = []
    for q in data_chart_date:
        date.append(q['date'].strftime('%Y-%m-%d'))
        net_amount.append(float(q['pricee']))

    print(date, net_amount)

    return render(request, "finance/tracking/asset_income.html",
                  context={'data': data, 'asset_form': asset_form, 'date': date, 'net_amount': net_amount, })


@login_required
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
    data_chart_date = PayableAccount.objects.values('date').order_by('date').annotate(pricee=Sum('price'))[:20]
    date = []
    net_amount = []
    for q in data_chart_date:
        date.append(q['date'].strftime('%Y-%m-%d'))
        net_amount.append(float(q['pricee']))

    print(date, net_amount)
    return render(request, "finance/tracking/expenditure.html",
                  context={'data': data, 'payable_account_form': payable_account_form, 'date': date, 'net_amount': net_amount, })


@login_required
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
    data_chart_date = Liability.objects.values('date').order_by('date').annotate(pricee=Sum('tax_levied'))[:20]
    date = []
    net_amount = []
    for q in data_chart_date:
        date.append(q['date'].strftime('%Y-%m-%d'))
        net_amount.append(float(q['pricee']))

    print(date, net_amount)
    return render(request, "finance/tracking/liabilities.html",
                  context={'data': data, 'liability_form': liability_form, 'date': date, 'net_amount': net_amount,})


@login_required
def finance_tracking(request):
    return render(request, "finance/tracking.html")


@login_required
def finance_reports(request):
    return render(request, "finance/reports.html")


@login_required
def finance_management(request):
    return render(request, "finance/management.html")


@login_required
def finance_ratios(request):
    return render(request, "finance/ratio.html")


@login_required
def finance_projection(request):
    return render(request, "finance/projections.html")


@login_required
def transactions(request):
    return render(request, "finance/tracking/transactions.html")



def finance_projection(request):
    share_funds = ShareholderFunds.objects.all()
    liability_source = LiabilitySources.objects.all()
    fund_application = FundApplication.objects.all()
    date = []
    net_amount = []
    for q in share_funds:
        date.append(q.year.year)
        net_amount.append(q.net_share_holding)

    date1 = []
    net_amount1 = []
    for q in fund_application:
        date1.append(q.year.year)
        net_amount1.append(q.net_fund_application)

    date2 = []
    net_amount2 = []
    for q in liability_source:
        date2.append(q.year.year)
        net_amount2.append(q.net_liabilities)

    percent_growth = [ -100, -90, -80, -70,- 60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, ]





    previous_share_funds = share_funds[3].net_share_holding
    previous_liabilities = liability_source[3].net_liabilities
    previous_fund_application = fund_application[3].net_fund_application



    share_funds_projected = []
    liabilities_projected = []
    fund_application_projected = []
    estimated_profit = []

    print(previous_share_funds, previous_liabilities, previous_fund_application)

    for q in percent_growth:
        a=(previous_share_funds * q *0.01) + previous_share_funds
        share_funds_projected.append(a)
        b=(previous_liabilities * q *0.01) + previous_liabilities
        liabilities_projected.append(b)
        c=(previous_fund_application * q *0.01) + previous_fund_application
        fund_application_projected.append(c)
        estimated_profit.append(a-b*0.1-c*0.1)

    print(fund_application_projected)


    context={"date": date, "net_amount":net_amount, "date1": date1, "net_amount1":net_amount1, "date2": date2,
            "net_amount2":net_amount2, "share_funds":share_funds, "liability_source":liability_source,
            "fund_application":fund_application, "estimated_profit":estimated_profit, "share_funds_projected":share_funds_projected,
              "liabilities_projected": liabilities_projected, "fund_application_projected":fund_application_projected,"percent_growth":percent_growth,}
    return render(request, "finance/projections.html", context=context)

