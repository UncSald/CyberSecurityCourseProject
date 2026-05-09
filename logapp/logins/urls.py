from django.urls import path

from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('login/', views.login, name='login'),
    path('user/<str:name>/', views.user_view, name='user'),
    path('user/<str:name>/create_log/', views.create_log, name='create_log'),
    path('confirm_creation/', views.confirm_creation, name='confirm'),
    path('create_user',views.create_user, name='create_user'),
]