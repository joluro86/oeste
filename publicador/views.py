from django.shortcuts import get_object_or_404, render, redirect
from .models import Publicador
from .forms import PublicadorForm


def publicador_detail(request, pk):
    publicador = get_object_or_404(Publicador, pk=pk)
    return render(request, 'myapp/publicador_detail.html', {'publicador': publicador})

def crear_publicador(request):
    if request.method == 'POST':
        form = PublicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publicador_list')  # Redirige a una vista de lista de publicadores o la que prefieras
    else:
        form = PublicadorForm()
    
    return render(request, 'oeste/publicador_form.html', {'form': form})

