from django.http import HttpResponse
from .models import Todo
from django.template import RequestContext, loader


def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'todos': todos,
    })
    return HttpResponse(template.render(context))


def create(request):
    pass
