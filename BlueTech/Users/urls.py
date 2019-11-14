from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token

from . import views

app_name = "users"

urlpatterns = [
    path('', views.home, name='project_home'),
    path('token-auth/', obtain_jwt_token),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/homepage.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post_login', views.post_login, name='post_login'),
    path('profile/', views.profile, name='profile'),
    path('hr/', include('HR.urls'))
]
