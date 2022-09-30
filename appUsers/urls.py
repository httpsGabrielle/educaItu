from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('escolas/', views.escolas, name='escolas'),
    path('jogos/', views.jogos, name='jogos'),
    path('jogos/pendentes/', views.jogospendentes, name='jogos'),
    path('jogos/jogosedit/<int:id>', views.jogosedit, name='jogosedit'),
]