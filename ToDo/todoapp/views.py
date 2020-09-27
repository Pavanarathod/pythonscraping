from django.shortcuts import render , redirect
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Todo
# Create your views here.

def home(request):
    current_date = timezone.now()
    content = request.POST.get('content')
    created_obj = Todo.objects.create(added_date=current_date, text=content )

    length_of_todos = Todo.objects.all().count()

    todo_items = Todo.objects.all().order_by('-added_date')


    return render(request, 'todoapp/index.html',  {
        'todo_items': todo_items,
    })

def delete_todo(request, todo_id):
    print(todo_id)
    return HttpResponseRedirect('todoapp/index.html')
    
