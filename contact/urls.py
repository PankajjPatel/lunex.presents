from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('start-project/', views.start_project, name='start_project'),
    path('success/', views.contact_success, name='success'),
]
