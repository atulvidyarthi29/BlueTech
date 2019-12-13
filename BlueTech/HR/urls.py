from django.urls import path
from . import views

app_name = "hr"

urlpatterns = [
    # path('add_user/<uidb64>/<token>/', views.add_user, name='add_user'),
    path('dashboard/hr', views.hr_dashboard, name='hr_dashboard'),
    path('departments/<str:dept_name>/', views.depart, name='depart'),
    path('training/', views.TrainingView.as_view(), name='train'),
    path('training/add/', views.TrainingCreateView.as_view(), name='train_add'),
    path('training/<pk>/', views.TrainingDetailView.as_view(), name='train_detail'),
    path('training/<pk>/update/', views.TrainingUpdateView.as_view(), name='train_update'),
    path('meeting/', views.MeetingView.as_view(), name='meet'),
    path('meeting/add/', views.MeetingCreateView.as_view(), name='meet_add'),
    path('meeting/<pk>/', views.MeetingDetailView.as_view(), name='meet_detail'),
    path('meeting/<pk>/update/', views.MeetingUpdateView.as_view(), name='meet_update'),
    path('complaint/', views.ComplaintListView.as_view(), name='complaints'),
    path('complaint/add/', views.ComplaintCreateView.as_view(), name='complaints_add'),
    path('complaint/<pk>/', views.ComplaintDetailView.as_view(), name='complaints_detail'),
    path('complaint/<pk>/update/', views.ComplaintUpdateView.as_view(), name='complaints_update'),
    path('payroll/', views.payroll, name='payroll'),
    path('status/<pk>', views.status, name='status'),
    path('meetinglist/', views.meeting_list_post.as_view(), name='meetinglist'),
    path('traininglist/', views.training_list_post.as_view(), name='traininglist'),
    path('complaintlist/', views.complaint_list_post.as_view(), name='complaintlist'),
]
