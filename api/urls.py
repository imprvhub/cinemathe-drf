from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import register_user, login_user, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('api/register/', register_user),
    path('login/', login_user, name='login'),
    path('logout/', logout_user),
]
