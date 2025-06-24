from django.contrib import admin
from .models import Usuario, Consulta, Pago, Noticia, Afiliacion

admin.site.register(Usuario)
admin.site.register(Consulta)
admin.site.register(Pago)
admin.site.register(Noticia)
admin.site.register(Afiliacion)

# Register your models here.
