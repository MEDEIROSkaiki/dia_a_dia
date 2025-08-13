# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1. A raiz do site (homepage) agora é a nossa página de entrada
    path('', views.landing_page, name='home'),
    
    # 2. A lista de eventos (o blog) foi movida para o endereço /blog/
    path('blog/', views.recipe_list, name='event_list'),
    
    # 3. A página de detalhes de um evento agora fica dentro de /blog/
    path('blog/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]