from django.urls import path
from . import views

urlpatterns = [
    path('', views.help_request_list, name='help_list'),
    path('add/', views.add_help_request, name='add_help'),
    path('register/', views.register, name='register'),

    path('help/<int:pk>/', views.take_help_request, name='take_help'),
    path('resolve/<int:pk>/', views.resolve_request, name='resolve'),

    path('dashboard/', views.dashboard, name='dashboard'),
]
