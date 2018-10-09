from django.shortcuts import render
from django.http import HttpResponse

from.models import Todo
# homepage


def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
    else:
        return render(request, 'add.html')
