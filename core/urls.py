from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('free-demo/', views.free_demo, name='free_demo'),

    # Legal pages
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('refund-and-cancellation/', views.refund_policy, name='refund_policy'),
    path('service-and-payment-policy/', views.payment_policy, name='payment_policy'),
]
