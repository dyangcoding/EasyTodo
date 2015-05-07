from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, CreateView, RedirectView, UpdateView

from EasyTodoLib.models import Todo

todoFields = ['title', 'deadline', 'done']


class TodosIndex(ListView):
    model = Todo
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TodosIndex, self).get_context_data(**kwargs)
        context['todos'] = self.model.objects.order_by('deadline')
        return context


class TodosCreate(CreateView):
    model = Todo
    fields = todoFields
    template_name = 'new.html'
    success_url = reverse_lazy('index')


class TodosEdit(UpdateView):
    model = Todo
    fields = todoFields
    template_name = 'edit.html'

    def get_success_url(self):
        return reverse_lazy('index')


class TodosDelete(RedirectView):
    model = Todo

    def get_redirect_url(self, pk=None):
        if pk != None:
            Todo.objects.get(pk=pk).delete()
            return reverse_lazy('index')


def impressum(request):
    template = loader.get_template('impressum.html')
    return HttpResponse(template.render())
