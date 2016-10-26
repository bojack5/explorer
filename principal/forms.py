from django import forms
from principal.models import *

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre','email','telefono','comentario',)
    