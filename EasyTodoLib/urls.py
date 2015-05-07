from django.conf.urls import url

from . import views
from EasyTodoLib.views import TodosIndex, TodosCreate, TodosDelete, TodosEdit

urlpatterns = [
    url(r'^$', TodosIndex.as_view(), name='index'),
    url(r'^new', TodosCreate.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/edit/$', TodosEdit.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', TodosDelete.as_view(), name='delete'),
    url(r'^impressum$', views.impressum, name='impressum')
]

handler404 = 'views.custom404'
