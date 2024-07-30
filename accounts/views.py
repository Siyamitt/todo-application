from django.shortcuts import render, redirect
from .models import Todo

# =================================== VIEWS HERE =========================

def home(request):    
    return render(request, "home.html")

# ====================================== TODO =========================================

def todo(request):
    
    todos = Todo.objects.all()
    incomplete_todos = todos.filter(is_completed = False)
    completed_todos = todos.filter(is_completed = True)
    
    parameters = {
        "todos": incomplete_todos,
        "completed_todos" :completed_todos
    }
    
    return render(request, "todo.html", parameters)

# ===================================== ADD TODO =======================================

def add_todo(request):
    
    if request.method == "POST":
        
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        new_todo = Todo(task=user_task, created_at=user_created_at)
        new_todo.save()
        
        return redirect("todo")
        
    return render(request, "add_todo.html")

def delete_todo(request,todo_id):
    del_todo = Todo.objects.get(id = todo_id)
    del_todo.delete()

    return redirect("todo")

def update_todo(request,todo_id):
    todo  = Todo.objects.get(id = todo_id)
    context = {
        "todo" : todo
    }

    if request.method == "POST":
        update_task = request.POST.get("task")
        date = request.POST.get("created_at")

        todo.task = update_task
        todo.created_at = date 
        todo.save()
        return redirect("todo")
    return render(request,"update_todo.html",context)


def complete_todo(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.is_completed = True
    todo.save()
    return redirect("todo")
















