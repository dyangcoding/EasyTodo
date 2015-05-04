from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index.as_view()),
    url(r'^create$', views.create.as_view()),
]
