from django.urls import path

from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('user/<str:name>/', views.user_view, name='user'),
    path('create_log/', views.create_log, name='create_log'),
    path('confirm_creation/', views.confirm_creation, name='confirm'),
    path('toplist/', views.most_hours, name='toplist')
]