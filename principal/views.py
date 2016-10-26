from django.shortcuts import render

from django.http import HttpResponse
from principal.forms import ComentarioForm

def index(request):
    form = ComentarioForm()

    return render(request, 'principal/index.html' , {'form':form})

def add_comentario(request):
    form = ComentarioForm()


    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return index(request)

        else:
            print(form.errors)

    return render(request , 'principal/index.html' , {'form':form})            