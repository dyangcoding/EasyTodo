from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, CreateView

from EasyTodoLib.models import Todo


class TodosIndex(ListView):
    model = Todo
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TodosIndex, self).get_context_data(**kwargs)
        context['todos'] = self.model.objects.order_by('deadline')
        return context


class TodosCreate(CreateView):
    model = Todo
    fields = ['title', 'deadline', 'done']
    template_name = 'new.html'
    success_url = 'index'

    def get_success_url(self):
        return reverse('index')


def impressum(request):
    template = loader.get_template('impressum.html')
    return HttpResponse(template.render())
