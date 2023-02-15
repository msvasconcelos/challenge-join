from django.shortcuts import render, get_object_or_404, redirect
from .models import Alvo
from .forms import AlvoForm


def listar_alvos(request):
    alvos = Alvo.objects.all()
    return render(request, 'alvos/listar_alvos.html', {'alvos': alvos})


def criar_alvo(request):
    if request.method == 'POST':
        form = AlvoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alvos')
    else:
        form = AlvoForm()
    return render(request, 'alvos/criar_alvo.html', {'form': form})


def editar_alvo(request, id):
    alvo = get_object_or_404(Alvo, id=id)
    if request.method == 'POST':
        form = AlvoForm(request.POST, instance=alvo)
        if form.is_valid():
            form.save()
            return redirect('listar_alvos')
    else:
        form = AlvoForm(instance=alvo)
    return render(request, 'alvos/editar_alvo.html', {'form': form})


def excluir_alvo(request, id):
    alvo = get_object_or_404(Alvo, id=id)
    alvo.delete()
    return redirect('listar_alvos')
