from django.urls import path
from . import views

app_name = 'audit'

urlpatterns = [
    path('', views.audit_home, name='home'),
    path('scan/', views.start_scan, name='start_scan'),
    path('report/<uuid:scan_id>/', views.audit_report, name='report'),
    path('dashboard/', views.audit_dashboard, name='dashboard'),
    path('toggle-resolution/<int:finding_id>/', views.toggle_resolution, name='toggle_resolution'),
]

