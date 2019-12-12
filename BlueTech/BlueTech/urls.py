from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import  obtain_jwt_token
app_name = "bluetech"

urlpatterns = [

    path('token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('finance/', include('finance.urls')),
    path('sales/', include('Sales.urls')),
    path('', include('Users.urls')),
]
