from django.shortcuts import render


# Create your views here.

def finance_home(request):
    department = request.user.employee.dept
    return render(request, "finance/home.html",
                  context={'department': department, 'user': request.user.employee})


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


def income(request):
    return render(request, "finance/tracking/income.html")


def expenditure(request):
    return render(request, "finance/tracking/expenditure.html")


def assets(request):
    return render(request, "finance/tracking/assets.html")


def liabilities(request):
    return render(request, "finance/tracking/liabilities.html")


def payables(request):
    return render(request, "finance/tracking/payables.html")


def recivables(request):
    return render(request, "finance/tracking/assets/recivables.html")


def current_assets(request):
    return render(request, "finance/tracking/assets/current_assets.html")


def intangible_assets(request):
    return render(request, "finance/tracking/assets/intangible_assets.html")


def investments(request):
    return render(request, "finance/tracking/assets/investments.html")


def current_liabilities(request):
    return render(request, "finance/tracking/liabilities/current_liabilities.html")


def longterm_liabilities(request):
    return render(request, "finance/tracking/liabilities/longterm_liabilities.html")


def stockholders_equity(request):
    return render(request, "finance/tracking/liabilities/stockholders_equity.html")


def ten_days_transactions(request):
    return render(request, "finance/tracking/transactions/ten_days.html")


def thirty_days_transactions(request):
    return render(request, "finance/tracking/transactions/thirty_days.html")


def four_months_transactions(request):
    return render(request, "finance/tracking/transactions/four_months.html")


def six_months_transactions(request):
    return render(request, "finance/tracking/transactions/six_months.html")


def one_year_transactions(request):
    return render(request, "finance/tracking/transactions/one_year.html")
