from django.urls import path
from .views import CrearMensajeView, ver_mensajes_recibidos, ver_mensajes_enviados, EliminarMensajeView

urlpatterns = [
    path('', CrearMensajeView.as_view(), name='crear_mensaje'),  # Ajusta según la página de inicio que quieras mostrar
    path('crear/', CrearMensajeView.as_view(), name='crear_mensaje'),
    path('recibidos/', ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('enviados/', ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('eliminar/<int:pk>/', EliminarMensajeView.as_view(), name='eliminar_mensaje'),
]