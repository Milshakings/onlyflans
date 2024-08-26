from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('contacto/', views.contacto, name='contacto'),
    path('success/<str:correo>/<str:nombre>/', views.success, name='success'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/', logout_view, name='logout'),
    path('comunity/',views.comunity, name = 'comunity'),
]
    # ...

