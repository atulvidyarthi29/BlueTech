from django.urls import path
from . import views

app_name = "hr"

urlpatterns = [
    # path('recruit/<str:dept_name>', views.recruit, name='recruit')
    path('departments/', views.departments, name='departments'),
    path('departments/<str:dept_name>', views.depart, name='depart'),
    path('job_vacancy', views.job_vacancy, name='job_vacancy'),
    path('job_applications', views.job_applications, name='job_applications'),
]
