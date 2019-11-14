from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.mail import send_mail
from .forms import UserRegistrationForm, ProductKeyForm, ProfileEditForm
from .models import License, Employee
from django.contrib.auth.decorators import login_required


def home(request):
    if not request.user.is_anonymous:
        return redirect('users:dashboard')
    try:
        license_obj = License.objects.first()
        validated = license_obj.validated
    except:
        validated = False
    return render(request, 'home/homepage.html', context={'validated': validated, 'true': True})


@login_required
def dashboard(request):
    try:
        department = request.user.employee.dept
        return render(request, 'home/dashboard.html', context={'department': department, 'user': request.user.employee})
    except:
        return render(request, 'home/404.html')


@login_required
def post_login(request):
    try:
        is_profile_complete = request.user.employee
    except:
        is_profile_complete = False
    if is_profile_complete:
        return redirect('users:dashboard')
    return redirect('users:profile')


@login_required
def profile(request):
    print('Submitted')
    if request.method == 'POST':
        try:
            profile_edit_form = ProfileEditForm(request.POST, request.FILES,
                                                instance=Employee.objects.get(user=request.user))
        except:
            profile_edit_form = ProfileEditForm(request.POST, request.FILES)
        user_form = UserRegistrationForm(request.POST, instance=request.user)
        if profile_edit_form.is_valid():
            print('valid')
            form_object = profile_edit_form.save(commit=False)
            form_object.user = request.user
            if profile_edit_form.cleaned_data['dept'] == 'CEO':
                form_object.reporting_to = None
            if profile_edit_form.cleaned_data['dept'] and profile_edit_form.cleaned_data['gender'] and \
                    profile_edit_form.cleaned_data['date'] and profile_edit_form.cleaned_data['date_of_joining'] and \
                    profile_edit_form.cleaned_data['phone_no']:
                form_object.is_complete = True
            else:
                form_object.is_complete = False
            form_object.is_verified = True
            form_object.save()
            return redirect('users:dashboard')
        print(profile_edit_form.errors)
        return render(request, 'users/profile.html', {'profile_edit_form': profile_edit_form, 'user_form': user_form,
                                                      'errors': profile_edit_form.errors})

    else:
        profile_edit_form = ProfileEditForm()
        user_form = UserRegistrationForm(instance=request.user)

    return render(request, 'users/profile.html', {'profile_edit_form': profile_edit_form, 'user_form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        key_form = ProductKeyForm(request.POST)
        if key_form.is_valid() and user_form.is_valid():
            pd_key = key_form.cleaned_data['product_key']
            lic_obj = License.objects.first()
            if lic_obj.licence == pd_key:
                lic_obj.validated = True
                lic_obj.save()
                user_form.save()
                login_user = authenticate(username=user_form.cleaned_data['username'],
                                          password=user_form.cleaned_data['password1'], )
                login(request, login_user)
                return redirect('users:post_login')
            return render(request, 'users/register.html',
                          {'user_form': user_form, 'key_form': key_form, 'errors': "Unauthorized"})
    else:
        user_form = UserRegistrationForm()
        key_form = ProductKeyForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'key_form': key_form})
