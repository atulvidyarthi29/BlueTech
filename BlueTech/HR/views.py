from collections import defaultdict
import json
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views import generic
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse

from django.db.models import Count
from rest_framework import generics

from rest_framework.views import APIView
from HR.forms import EmailsForm, PayrollForm
from HR.models import Meeting, Training
from HR.tokens import recruitment_token
from Users.forms import UsersTemp
from Users.models import Employee
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics

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
    members_list = [len(Employee.objects.filter(dept='SALES')), len(Employee.objects.filter(dept='ACCOUNTS')),
                    len(Employee.objects.filter(dept='HR'))]
    print(members_list)
    today = datetime.datetime.now()
    # queryset = Training.objects.values('start_date').filter(start_date__year=today.year).order_by(
    #     'start_date__year').annotate(
    #     cout=Count('id'))
    date_recruit = Employee.objects.values('date').filter(date__year=today.year).order_by(
        'date__year').annotate(
        dcount=Count('id'))[:20]
    cv = defaultdict(int)
    for i in range(12):
        x = Employee.objects.filter(date_of_joining__month=i + 1)
        cv[i + 1] = len(x)
    cv0 = list(cv.keys())
    cv1 = list(cv.values())
    cv0 = json.dumps(cv0)
    cv1 = json.dumps(cv1)
    date = []
    net_amount = []
    for q in date_recruit:
        date.append(q['date'].month)
        net_amount.append(q['dcount'])

    return render(request, 'HR/past_recruitment.html',
                  context={'department': department,
                           'user': request.user.employee, 'members': members,
                           'users_temp': users_temp,
                           'email_form': email_form,
                           'lines': lines,
                           'members_list': members_list,
                           'date': date,
                           'net_amount': net_amount,
                           'cv0': cv0,
                           'cv1': cv1,
                           })


@login_required
def hr_dashboard(request):
    department = request.user.employee.dept
    return render(request, 'HR/dashboard.html',
                  context={'department': department, 'user': request.user, })



@login_required
def recruit(request):
    department = request.user.employee.dept
    members_list = [len(Employee.objects.filter(dept='SALES')), len(Employee.objects.filter(dept='ACCOUNTS')),
                    len(Employee.objects.filter(dept='HR'))]
    print(members_list)
    return render(request, 'HR/recruitment.html',
                  context={'department': department, 'user': request.user.employee, 'members_list': members_list})





@login_required
def payroll(request):
    department = request.user.employee.dept
    if request.method == 'POST':
        payroll_form = PayrollForm(request.POST)
        if payroll_form.is_valid():
            payroll_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        payroll_form = PayrollForm()

    salary = Salary.objects.all()
    return render(request, 'HR/payroll.html',
                  context={'department': department, 'payroll_form': payroll_form, 'payroll': salary})


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


# class MeetingDeleteView(DeleteView):
#     model=Meeting
#     success_url = reverse('user:hr:meet')
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['department'] = self.request.user.employee.dept
#         return context


class TrainingView(generic.ListView):
    template = 'HR/training_list.html'

    def get_queryset(self):
        return Training.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.datetime.now()
        queryset = Training.objects.values('start_date').filter(start_date__year=today.year).order_by(
            'start_date__year').annotate(
            cout=Count('id'))
        print(queryset)
        date = []
        count = []
        for q in queryset:
            date.append(q['start_date'].month)
            count.append(q['cout'])
        print(date)
        print(count)
        cv = defaultdict(int)
        for i in range(12):
            x = Training.objects.filter(start_date__month=i + 1)
            cv[i + 1] = len(x)
        cv0 = list(cv.keys())
        cv1 = list(cv.values())
        cv0 = json.dumps(cv0)
        cv1 = json.dumps(cv1)
        context['date'] = date
        context['count'] = count
        context['cv0'] = cv0
        context['cv1'] = cv1
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

class ComplaintCreateView(CreateView):
    model = Complaint
    fields = ['by', 'against', 'complain']

    def get_success_url(self):
        return reverse('users:dashboard')

    # def form_valid(self, form):
    #     form.instance.employee = self.request.employee
    #     return super(ComplaintCreateView, self).form_valid(form)


class ComplaintListView(generic.ListView):
    template = 'HR/complaints_list.html'

    def get_queryset(self):
        return Complaint.objects.all().order_by('status', '-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.request.user.employee.dept
        return context


class ComplaintDetailView(generic.DetailView):
    model = Complaint
    template = 'HR/complaints_detail.html'


class ComplaintUpdateView(UpdateView):
    model = Complaint
    fields = '__all__'


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

class meeting_list_post(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class training_list_post(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class complaint_list_post(generics.ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

def status(request, pk):
    a = get_object_or_404(Complaint, id=pk)
    if a.status == 'Pending':
        a.status = 'Resolved'
    a.save()
    return redirect(request.META.get('HTTP_REFERER'))



class meeting_list(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    lookup_field = 'location'


class meeting_list_post(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class training_list_post(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class complaint_list_post(generics.ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
