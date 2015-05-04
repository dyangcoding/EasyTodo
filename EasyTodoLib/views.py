from django.views.generic import CreateView

from django.views.generic import ListView

from EasyTodoLib.models import ToDo


class index(ListView):
    template_name = 'index.html'
    model = ToDo

class create(CreateView):
    template_name = 'new.html'
    model = ToDo
    success_url = '/'
