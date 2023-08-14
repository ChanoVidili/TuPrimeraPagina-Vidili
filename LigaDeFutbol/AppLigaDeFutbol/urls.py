from django.urls import path
from AppLigaDeFutbol import views


urlpatterns = [
    path('', views.buscar_jugadores_por_nombre, name="Inicio"),
    path('jugadorFormulario/', views.agregar_jugador, name="JugadorFormulario"),
    path('dtFormulario/', views.agregar_director_tecnico, name="DTFormulario"),
    path('clubFormulario/', views.agregar_club, name="ClubFormulario"),
    path('buscarPorNombre/', views.buscar_jugadores_por_nombre, name='BuscarJugadoresPorNombre'),
]