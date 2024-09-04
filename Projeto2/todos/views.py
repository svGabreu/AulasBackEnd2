from django.shortcuts import render

from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


#def home(request):
#    return render(request, "todos/home.html")

#def todo_list(request):
#    nome = 'Rodrigo'
#    alunos = ['1. Ana', '2. José', '3. Bia']
#    return render(request, "todos/todo_list.html", {"nome": nome, "lista_alunos": alunos})



#def todo_list_old(request):
#    nome = 'Rodrigo'
#    alunos = ['1. Ana', '2. José', '3. Bia']
#    return render(request, "todos/todo_list.html", {"nome": nome, "lista_alunos": alunos})

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
