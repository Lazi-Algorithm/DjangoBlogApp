
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members.views import PasswordsChangeView
from members import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members', include('members.urls')),
    path('password/',PasswordsChangeView.as_view(template_name = 'registration/change_password.html')),
    path('password_success', views.password_success, name='password_success')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
