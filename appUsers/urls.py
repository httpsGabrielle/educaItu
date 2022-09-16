from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('escolas/', views.escolas, name='escolas'),

]