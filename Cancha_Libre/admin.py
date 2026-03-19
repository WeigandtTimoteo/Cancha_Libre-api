from django.contrib import admin
from .models import Usuario, Jugador, Posicion, RolPos, UsuarioPosicion, JugadorPosicion

# Registramos cada modelo para que aparezca en el panel
admin.site.register(Usuario)
admin.site.register(Jugador)
admin.site.register(Posicion)
admin.site.register(RolPos)
admin.site.register(UsuarioPosicion)
admin.site.register(JugadorPosicion)