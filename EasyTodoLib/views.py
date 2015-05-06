from django.forms import BaseForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'todos': todos,
    })
    return HttpResponse(template.render(context))


def new(request):
    form = BaseForm()
    return render_to_response('new.html', {'form': form}, context_instance=RequestContext(request))


def impressum(request):
    template = loader.get_template('impressum.html')
    return HttpResponse(template.render())
