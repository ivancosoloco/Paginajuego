from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='appcosoloco/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.inicio, name='inicio'),
    path('historia/', views.historia, name='historia'),
    path('desarrollo/', views.desarrollo, name='desarrollo'),
    path('contacto/', views.contacto, name='contacto')
]