from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"

urlpatterns = [
    path('', views.home, name='project_home'),
    path('add_user/<uidb64>/<token>/', views.add_user, name='add_user'),
    # path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/homepage.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/ceo', views.ceo_dashboard, name='ceo_dashboard'),
    path('post_login/<dept>/', views.post_login, name='post_login'),
    path('to_post_login/', views.to_post_login, name='to_post_login'),
    path('profile/<dept>/', views.profile, name='profile'),
    path('profile/update/<pk>/', views.update_profile, name='update'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('hr/', include('HR.urls')),
    path('team/', views.team, name='team'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('thank-you/', views.boot_start, name='boot_start'),
    path('sending-mail/<str:un>/', views.send_ceo_method, name='send_ceo_method'),
]
