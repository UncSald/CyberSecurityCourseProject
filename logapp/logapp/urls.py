from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<str:name>/logout/', LogoutView.as_view(next_page='/')),
    path('', include('logins.urls')),   
]
