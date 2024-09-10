from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Mensaje
from .forms import MensajeForm


class CrearMensajeView(View):
    def get(self, request):
        form = MensajeForm()
        return render(request, 'mensajes/crear_mensaje.html', {'form': form})

    def post(self, request):
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('ver_mensajes_enviados')
        return render(request, 'mensajes/crear_mensaje.html', {'form': form})

def ver_mensajes_recibidos(request):
    if request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(destinatario=request.user)
    else:
        mensajes = []
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})

def ver_mensajes_enviados(request):
    if request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(remitente=request.user)
    else:
        mensajes = []  
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

class EliminarMensajeView(DeleteView):
    model = Mensaje
    success_url = reverse_lazy('ver_mensajes_recibidos')
    
