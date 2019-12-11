# <<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import SalesForm, AssetForm, PayableAccountForm, LiabilityForm
from .models import SalesAccount, Asset, PayableAccount, Liability
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
        return HttpResponse("Some Error Occurred")
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

    return render(request, "finance/tracking/asset_income.html",
                  context={'data': data, 'asset_form': asset_form})


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
    return render(request, "finance/tracking/expenditure.html",
                  context={'data': data, 'payable_account_form': payable_account_form})


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
    return render(request, "finance/tracking/liabilities.html",
                  context={'data': data, 'liability_form': liability_form})


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
# =======
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.db.models import Sum
# from .forms import SalesForm, AssetForm, PayableAccountForm, LiabilityForm
# from .models import SalesAccount, Asset, PayableAccount, Liability
# from datetime import date
# from django.contrib.auth.decorators import login_required
#
#
# # Create your views here.
#
# @login_required
# def finance_home(request):
#     department = request.user.employee.dept
#     return render(request, "finance/home.html",
#                   context={'department': department, 'user': request.user.employee})
#
#
# @login_required
# def income(request):
#     if request.method == 'POST':
#         sales_form = SalesForm(request.POST)
#         if sales_form.is_valid():
#             sales_form.save()
#             return redirect(request.META.get('HTTP_REFERER'))
#         return HttpResponse("Some Error Occured")
#     else:
#         sales_form = SalesForm()
#     data = SalesAccount.objects.all()
#     data_chart_date = SalesAccount.objects.values('date').order_by('date').annotate(pricee=Sum('price'))[:20]
#     date = []
#     net_amount = []
#     for q in data_chart_date:
#         date.append(q['date'].strftime('%Y-%m-%d'))
#         net_amount.append(q['pricee'])
#
#     print(date, net_amount)
#     return render(request, "finance/tracking/income.html",
#                   context={'data': data, 'sales_form': sales_form, 'date': date, 'net_amount': net_amount, })
#
#
# @login_required
# def income_asset(request):
#     if request.method == 'POST':
#         asset_form = AssetForm(request.POST)
#         if asset_form.is_valid():
#             asset_form.save()
#             return redirect(request.META.get('HTTP_REFERER'))
#         return HttpResponse("Some Error occurred")
#     else:
#         asset_form = AssetForm()
#     data = Asset.objects.all()
#
#     return render(request, "finance/tracking/asset_income.html",
#                   context={'data': data, 'asset_form': asset_form})
#
#
# @login_required
# def expenditure(request):
#     if request.method == 'POST':
#         payable_account_form = PayableAccountForm(request.POST)
#         if payable_account_form.is_valid():
#             payable_account_form.save()
#             return redirect(request.META.get('HTTP_REFERER'))
#         return HttpResponse("Some Error Occured")
#     else:
#         payable_account_form = PayableAccountForm()
#     data = PayableAccount.objects.all()
#     return render(request, "finance/tracking/expenditure.html",
#                   context={'data': data, 'payable_account_form': payable_account_form})
#
#
# @login_required
# def liabilities(request):
#     if request.method == 'POST':
#         liability_form = LiabilityForm(request.POST)
#         if liability_form.is_valid():
#             liability_form.save()
#             return redirect(request.META.get('HTTP_REFERER'))
#         return HttpResponse("Some Error occurred")
#     else:
#         liability_form = LiabilityForm()
#     data = Liability.objects.all()
#     return render(request, "finance/tracking/liabilities.html",
#                   context={'data': data, 'liability_form': liability_form})
#
#
# @login_required
# def finance_tracking(request):
#     return render(request, "finance/tracking.html")
#
#
# @login_required
# def finance_reports(request):
#     return render(request, "finance/reports.html")
#
#
# @login_required
# def finance_management(request):
#     return render(request, "finance/management.html")
#
#
# @login_required
# def finance_ratios(request):
#     return render(request, "finance/ratio.html")
#
#
# @login_required
# def finance_projection(request):
#     return render(request, "finance/projections.html")
#
#
# @login_required
# def transactions(request):
#     return render(request, "finance/tracking/transactions.html")
# >>>>>>> 22986b0c624a63ecf011ca56a803c1a366725f6c
