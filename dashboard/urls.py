from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.dashboard_login, name='login'),
    path('logout/', views.dashboard_logout, name='logout'),
    path('', views.dashboard_home, name='home'),
    path('enquiries/', views.enquiries_list, name='enquiries'),
    path('enquiries/<int:pk>/', views.enquiry_detail, name='enquiry_detail'),
    path('enquiries/<int:pk>/mark-read/', views.enquiry_mark_read, name='enquiry_mark_read'),
    path('reviews/', views.reviews_list, name='reviews'),
    path('reviews/<int:pk>/approve/', views.review_toggle_approve, name='review_approve'),
    path('reviews/<int:pk>/verify/', views.review_toggle_verify, name='review_verify'),
    path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/add/', views.portfolio_add, name='portfolio_add'),
    path('portfolio/<int:pk>/edit/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolio/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
    path('services/', views.services_list, name='services'),
]

