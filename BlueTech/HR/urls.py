from django.urls import path
from . import views

app_name = "hr"

urlpatterns = [
    # path('add_user/<uidb64>/<token>/', views.add_user, name='add_user'),
    path('recruit/', views.recruit, name='recruit'),
    path('dashboard/hr', views.hr_dashboard, name='hr_dashboard'),
    path('departments/<str:dept_name>/', views.depart, name='depart'),
    path('training/', views.TrainingView.as_view(), name='train'),
    path('training/add/', views.TrainingCreateView.as_view(), name='train_add'),
    path('training/<pk>/', views.TrainingDetailView.as_view(), name='train_detail'),
    path('meeting/', views.MeetingView.as_view(), name='meet'),
    path('meeting/add/', views.MeetingCreateView.as_view(), name='meet_add'),
    path('meeting/<pk>/', views.MeetingDetailView.as_view(), name='meet_detail'),
    path('job_vacancy/', views.job_vacancy, name='job_vacancy'),
    path('job_applications/', views.job_applications, name='job_applications'),
]
