from django.contrib import admin
from principal.models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'email' , )

admin.site.register(Comentario,ComentarioAdmin)

# Register your models here.
