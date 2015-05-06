from django.conf.urls import url

from . import views
from EasyTodoLib.views import TodosIndex, TodosCreate

urlpatterns = [
    url(r'^$', TodosIndex.as_view(), name='index'),
    url(r'^new', TodosCreate.as_view(), name='new'),
    url(r'^impressum$', views.impressum, name='impressum')
]
