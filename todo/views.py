from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(req):
    todos = Todo.objects.all()
    return render(req, "index.html", {"todos": todos, "title": "Home"})

def add(req):

    if req.method == "POST":
        todo = TodoForm(req.POST)
        todo.save()
        return redirect("index")
    else:
        return render(req, "add.html", {"title": "Add"})

def edit(req, pk):

    todo = get_object_or_404(Todo, pk=pk)
    # changing the format (for example March 9, 2023 will change into 2023-03-09)
    todo.deadline = todo.deadline.strftime("%Y-%m-%d")
    

    if req.method == "POST":
        todo = TodoForm(req.POST, instance=todo)
        todo.save()
        return redirect("index")
    else:
        return render(req, "edit.html", {"todo": todo, "title": "Edit"})

def delete(req, pk):

    Todo.objects.filter(pk=pk).delete()
    return redirect("index")


