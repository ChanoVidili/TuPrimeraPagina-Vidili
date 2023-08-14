from django.shortcuts import render, redirect
from AppLigaDeFutbol.forms import JugadorFormulario, DirectorTecnicoFormulario, ClubFormulario, JugadorBusquedaFormulario
from .models import Jugador


def inicio(request):
    return render(request, "inicio.html")

def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = JugadorFormulario()
    return render(request, 'jugador_formulario.html', {'form': form})


def agregar_director_tecnico(request):
    if request.method == 'POST':
        form = DirectorTecnicoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = DirectorTecnicoFormulario()
    return render(request, 'director_tecnico_formulario.html', {'form': form})


def agregar_club(request):
    if request.method == 'POST':
        form = ClubFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = ClubFormulario()
    return render(request, 'club_formulario.html', {'form': form})


def buscar_jugadores_por_nombre(request):
    jugadores = []
    form = JugadorBusquedaFormulario(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Jugador por nombre
        if nombre:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_jugadores.html', {'form': form, 'jugadores': jugadores})