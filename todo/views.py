from django.shortcuts import render,redirect
from todo.forms import TodoForm

from todo.models import Todo

def home(request):
  todos = Todo.objects.all()
  context = {
    "todos":todos
  }
  return render(request, "todo/home.html", context)


def todo_create(request):
  form = TodoForm()

  if request.method == "POST":
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("home")
      
  context = {
    "form":form
  }
  return render(request, "todo/todo_add.html", context)
