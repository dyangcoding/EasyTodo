from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from EasyTodoLib.models import ToDo
# Create your views here.

class IndexView(ListView):
	template_name = 'home.html'
	model = ToDo
	
class CreateToDo(CreateView):
	template_name = 'new.html'
	model = ToDo
	success_url = '/'