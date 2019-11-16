from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views import generic
from django.views.generic import UpdateView, CreateView
from django.urls import reverse
from rest_framework.views import APIView
from HR.forms import EmailsForm
from HR.models import Meeting, Training
from HR.tokens import recruitment_token
from Users.forms import UsersTemp
from Users.models import Employee
from .serializers import *
from rest_framework.response import Response


@login_required
def depart(request, dept_name):
    lines = None
    if request.method == 'POST':
        users_temp = UsersTemp(request.POST)
        email_form = EmailsForm(request.POST, request.FILES)
        if users_temp.is_valid():
            users_temp.save()
            to_email = users_temp.cleaned_data.get('email')
            department = users_temp.cleaned_data.get('dept')
            tup = str(to_email) + ' ' + str(department)
            current_site = get_current_site(request)
            mail_subject = 'Join using this link!'
            message = render_to_string('hr/recruitment_email.html', {
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(tup)),
                'token': recruitment_token.make_token((to_email, department)),
            })

            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect(request.META.get('HTTP_REFERER'))
        if email_form.is_valid():
            email_form = email_form.save()
            with open(email_form.file.url, 'r') as csv_file:
                lines = csv_file.readlines()
                del lines[0]
                for line in lines:
                    lt = line.strip('\n').split(',')
                    tup = str(lt[0]) + ' ' + str(lt[1])
                    current_site = get_current_site(request)
                    mail_subject = 'Join using this link!'
                    message = render_to_string('hr/recruitment_email.html', {
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(tup)),
                        'token': recruitment_token.make_token(tup),
                    })

                    email = EmailMessage(
                        mail_subject, message, to=[lt[0]]
                    )
                    email.send()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        users_temp = UsersTemp()
        email_form = EmailsForm()
    department = request.user.employee.dept
    members = Employee.objects.filter(dept=dept_name)
    return render(request, 'HR/past_recruitment.html',
                  context={'department': department,
                           'user': request.user.employee, 'members': members,
                           'users_temp': users_temp,
                           'email_form': email_form,
                           'lines': lines})


@login_required
def recruit(request):
    department = request.user.employee.dept
    return render(request, 'HR/recruitment.html',
                  context={'department': department, 'user': request.user.employee, })


@login_required
def hr_dashboard(request):
    department = request.user.employee.dept
    return render(request, 'HR/dashboard.html',
                  context={'department': department, 'user': request.user.employee, })


@login_required
def job_vacancy(request):
    department = request.user.employee.dept
    return render(request, 'HR/job_posted.html',
                  context={'department': department, 'user': request.user.employee, })


@login_required
def job_applications(request):
    department = request.user.employee.dept
    return render(request, 'HR/job_applications.html',
                  context={'department': department, 'user': request.user.employee, })


class MeetingView(generic.ListView):
    template = 'HR/meeting_list.html'

    def get_queryset(self):
        return Meeting.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context


class MeetingDetailView(generic.DetailView):
    model = Meeting
    template = 'HR/meeting_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context


class MeetingCreateView(CreateView):
    model = Meeting
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context

    def get_success_url(self):
        return reverse('users:hr:meet')


class MeetingUpdateView(UpdateView):
    model = Meeting
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context

    def get_success_url(self):
        return reverse('users:hr:meet')


class TrainingView(generic.ListView):
    template = 'HR/training_list.html'

    def get_queryset(self):
        return Training.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context


class TrainingDetailView(generic.DetailView):
    model = Training
    template = 'HR/training_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context


class TrainingCreateView(CreateView):
    model = Training
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context

    def get_success_url(self):
        return reverse('users:hr:train')


class TrainingUpdateView(UpdateView):
    model = Training
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context

    def get_success_url(self):
        return reverse('users:hr:train')


class MeetingList(APIView):

    def get(self, request):
        meeting = Meeting.objects.all()
        serializer = MeetingSerializer(meeting, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
