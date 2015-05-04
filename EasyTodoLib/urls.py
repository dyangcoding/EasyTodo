__author__ = 'fabian082'
from django.conf.urls import patterns, url
from EasyTodoLib import views

urlpatterns = patterns('',
	url(r'^$',views.IndexView.as_view()),
	url(r'^create$', views.CreateToDo.as_view()),



	)