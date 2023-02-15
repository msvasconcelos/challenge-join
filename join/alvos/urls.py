from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alvos, name='lista_alvos'),
    path('novo/', views.novo_alvo, name='novo_alvo'),
    path('<int:pk>/edita/', views.edita_alvo, name='edita_alvo'),
    path('<int:pk>/exclui/', views.exclui_alvo, name='exclui_alvo'),
]
