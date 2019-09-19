from django.contrib import admin
from django.urls import path, include

app_name = "bluetech"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls'))
]
