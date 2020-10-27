from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt

from . import paytm_checksum
from . import payment_config
from .content import team_content, index_content
from .forms import UserRegistrationForm, ProductKeyForm, ProfileEditForm, PaymentForm
from .models import License, Employee
from .models import User


def buy_erp(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form = payment_form.save(commit=False)
            payment_form.validated = False
            payment_form.save()
            absolute_url = request.build_absolute_uri()[0:-1]
            CALLBACK_URL = absolute_url[0:absolute_url.rindex('/')] + '/handle_request/'
            print(CALLBACK_URL)
            param_dict = {
                'MID': payment_config.MID,
                'ORDER_ID': str(payment_form.licence),
                'TXN_AMOUNT': payment_config.TXN_AMOUNT,
                'CUST_ID': payment_form.email,
                'INDUSTRY_TYPE_ID': payment_config.INDUSTRY_TYPE_ID,
                'WEBSITE': payment_config.WEBSITE,
                'CHANNEL_ID': payment_config.CHANNEL_ID,
                'CALLBACK_URL': CALLBACK_URL,
            }
            print(param_dict)
            param_dict['CHECKSUMHASH'] = paytm_checksum.generateSignature(param_dict, payment_config.MERCHANT_KEY)

            return render(request, 'users/payment_processing.html', {'param_dict': param_dict})
    payment_form = PaymentForm()
    return render(request, "users/checkout_page.html", {'payment_form': payment_form})


@csrf_exempt
def handle_request(request):
    form = request.POST
    response = {}
    for key in form.keys():
        response[key] = form[key]
    check = response['CHECKSUMHASH']
    verify = paytm_checksum.verifySignature(response, payment_config.MERCHANT_KEY, check)
    print(response)
    if verify:
        if response['RESPCODE'] == '01':
            license_object = License.objects.get(licence=response['ORDERID'])
            send_email(request, license_object)
            return HttpResponse('Thank you for the payment. Please check your email for further instructions.')
        else:
            return HttpResponse("Something went wrong.")
    else:
        return HttpResponse("Checksum Verification failed")


def send_email(request, license_object):
    tup = str(license_object.email) + ' ' + 'CEO' + ' ' + str(license_object.licence)
    current_site = get_current_site(request)
    mail_subject = 'Join using this link!'
    message = render_to_string('hr/recruitment_email.html', {
        'unique_code': license_object.licence,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(tup)),
        'token': str(tup),
    })
    email = EmailMessage(
        mail_subject, message, to=[license_object.email]
    )
    email.send()


def home(request):
    if not request.user.is_anonymous:
        return redirect('users:dashboard')
    try:
        license_obj = License.objects.first()
        validated = license_obj.validated
    except:
        validated = False
    return render(request, 'home/homepage.html',
                  context={'validated': validated, 'true': True, 'content': index_content})


def team(request):
    if not request.user.is_anonymous:
        return redirect('users:dashboard')
    try:
        license_obj = License.objects.first()
        validated = license_obj.validated
    except:
        validated = False
    return render(request, 'home/team.html', context={'content': team_content, 'validated': validated})


def terms_of_service(request):
    if not request.user.is_anonymous:
        return redirect('users:dashboard')
    try:
        license_obj = License.objects.first()
        validated = license_obj.validated
    except:
        validated = False
    return render(request, 'home/terms_of_service.html', context={'validated': validated, })


def privacy_policy(request):
    if not request.user.is_anonymous:
        return redirect('users:dashboard')
    try:
        license_obj = License.objects.first()
        validated = license_obj.validated
    except:
        validated = False
    return render(request, 'home/privacy_policy.html', context={'validated': validated, })


def disclaimer(request):
    if not request.user.is_anonymous:
        return redirect('users:dashboard')
    try:
        license_obj = License.objects.first()
        validated = license_obj.validated
    except:
        validated = False
    return render(request, 'home/disclaimer.html', context={'validated': validated, })


def add_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64).decode())
        tup = uid.split()
        print(tup)
        if tup[1] == 'CEO':
            element = License.objects.get(licence=tup[2])
            element.validated = True
            element.save()
    except(TypeError, ValueError, OverflowError):
        return HttpResponse('Could not verify you!')

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form2 = user_form.save(commit=False)
            user_form2.is_active = True
            user_form2.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password1'])
            login(request, user)
            return redirect('users:post_login', tup[1])
        return render(request, 'users/register.html',
                      {'user_form': user_form, 'errors': "Unauthorized"})
    else:
        p = User()
        p.email = tup[0]
        user_form = UserRegistrationForm(instance=p)
        key_form = ProductKeyForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'key_form': key_form, 'dept': uid[1]})


@login_required
def to_post_login(request):
    return redirect('users:post_login', '-')


@login_required
def post_login(request, dept):
    try:
        is_profile_complete = request.user.employee.is_complete
    except:
        is_profile_complete = False
    if is_profile_complete:
        return redirect('users:dashboard')
    return redirect('users:profile', dept)


@login_required
def profile(request, dept):
    if request.method == 'POST':
        try:
            profile_edit_form = ProfileEditForm(request.POST, request.FILES,
                                                instance=Employee.objects.get(user=request.user))
        except:
            profile_edit_form = ProfileEditForm(request.POST, request.FILES)
        user_form = UserRegistrationForm(request.POST, instance=request.user)
        if profile_edit_form.is_valid():
            form_object = profile_edit_form.save(commit=False)
            form_object.dept = dept
            form_object.user = request.user
            if dept == 'CEO':
                form_object.reporting_to = None
            if form_object.dept and profile_edit_form.cleaned_data['gender'] and \
                    profile_edit_form.cleaned_data['date'] and profile_edit_form.cleaned_data['date_of_joining'] and \
                    profile_edit_form.cleaned_data['phone_no']:
                form_object.is_complete = True
            else:
                form_object.is_complete = False
            form_object.is_verified = False
            form_object.save()
            return redirect('users:dashboard')
        print(profile_edit_form.errors)
        return render(request, 'users/profile.html',
                      {'profile_edit_form': profile_edit_form, 'user_form': user_form,
                       'errors': profile_edit_form.errors, 'deptat': dept, })

    else:
        profile_edit_form = ProfileEditForm()
        user_form = UserRegistrationForm(instance=request.user)

    return render(request, 'users/profile.html',
                  {'profile_edit_form': profile_edit_form, 'user_form': user_form, 'dept': dept})


@login_required
def dashboard(request):
    try:
        department = request.user.employee.dept
        if department == 'CEO':
            return redirect('users:ceo_dashboard')
        elif department == 'HR':
            return redirect('users:hr:hr_dashboard')
        elif department == 'ACCOUNTS':
            return redirect('finance:finance_home')
        elif department == 'SALES':
            return redirect('sales:sales_dashboard')
    except:
        return render(request, 'home/404.html')


@login_required
def ceo_dashboard(request):
    department = request.user.employee.dept
    return render(request, 'home/dashboard.html',
                  context={'department': department, 'user': request.user})


@login_required
def update_profile(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    profile_update_form = ProfileEditForm(request.POST, request.FILES, instance=employee)
    if request.method == 'POST':
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'profile_update_form': profile_update_form,
        'department': request.user.employee.dept,
        'profile': employee,
        'user': request.user,
    }
    return render(request, 'users/profile_update.html', context)

# def boot_start(request):
#     if request.method == 'GET':
#         get_response = [request.GET.get('payment_id'), request.GET.get('status')]
#         print(get_response)
#         if len(get_response) == 2 and get_response[1] == 'success':
#             un = uuid.uuid4()
#             License.objects.create(licence=un, validated=False)
#             email_form = EmailForm()
#             return render(request, 'users/ceo_email_info.html', context={'email_form': email_form, 'un': str(un)})
#         else:
#             return render(request, 'home/404.html')
#     else:
#         return HttpResponse("Something went wrong!")
#
#
# def send_ceo_method(request, un):
#     if request.method == 'POST':
#         email_form = EmailForm(request.POST)
#         if email_form.is_valid():
#             to_email = email_form.cleaned_data['email']
#             tup = str(to_email) + ' ' + 'CEO' + ' ' + str(un)
#             current_site = get_current_site(request)
#             mail_subject = 'Join using this link!'
#             message = render_to_string('hr/recruitment_email.html', {
#                 'unique_code': un,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(tup)),
#                 'token': str(tup),
#             })
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Thank you for the payment. Please check your email for further instructions.')
#         redirect(request.META.get('HTTP_REFERER'))
#     else:
#         redirect(request.META.get('HTTP_REFERER'))


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         key_form = ProductKeyForm(request.POST)
#         if key_form.is_valid() and user_form.is_valid():
#             pd_key = key_form.cleaned_data['product_key']
#             lic_obj = License.objects.first()
#             if lic_obj.licence == pd_key:
#                 lic_obj.validated = True
#                 lic_obj.save()
#                 user_form2 = user_form.save(commit=False)
#                 user_form2.is_active = False
#                 user_form2.save()
#                 current_site = get_current_site(request)
#                 mail_subject = 'Please, verify your Email!'
#                 message = render_to_string('users/activate_email.html', {
#                     'user': user_form2,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user_form2.pk)).decode(),
#                     'token': account_activation_token.make_token(user_form2),
#                 })
#                 to_email = user_form.cleaned_data.get('email')
#                 email = EmailMessage(
#                     mail_subject, message, to=[to_email]
#                 )
#                 email.send()
#                 return HttpResponse('Please confirm your email address to complete the registration')
#             return render(request, 'users/register.html',
#                           {'user_form': user_form, 'key_form': key_form, 'errors': "Unauthorized"})
#     else:
#         user_form = UserRegistrationForm()
#         key_form = ProductKeyForm()
#     return render(request, 'users/register.html', {'user_form': user_form, 'key_form': key_form})
#
#
# def activate(request, uidb64, token):
#     try:
#         print(uidb64)
#         uid = force_text(urlsafe_base64_decode(uidb64).decode())
#         print(uid)
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('users:post_login', 'CEO')
#     else:
#         return HttpResponse('Activation link is invalid!')
