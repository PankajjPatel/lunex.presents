from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('start-project/', views.start_project, name='start_project'),
    path('free-demo/', views.free_demo_request, name='free_demo'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('success/', views.contact_success, name='success'),
]
