from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('historia/', views.historia, name='historia'),
    path('desarrollo/', views.desarrollo, name='desarrollo'),
    path('contacto/', views.contacto, name='contacto')
]