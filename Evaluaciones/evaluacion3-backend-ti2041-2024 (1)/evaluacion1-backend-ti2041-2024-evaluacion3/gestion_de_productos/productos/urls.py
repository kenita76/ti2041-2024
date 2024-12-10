from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("resultado/", views.resultado, name="resultado"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]