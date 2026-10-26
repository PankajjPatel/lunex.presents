from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.work, name='work'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]
